"""Read selected columns/row groups of a remote parquet file by HTTP range requests (no full download).
Usage: python3 -I hf_range.py <pylibs> <hf_resolve_url> [--cols a,b] [--rgs N]"""
import io
import sys
import time

import requests

sys.path.insert(0, sys.argv[1])
import pyarrow.parquet as pq  # noqa: E402


class RangeFile(io.RawIOBase):
    def __init__(self, url):
        r = requests.head(url, allow_redirects=True, timeout=60)
        self.url = r.url
        self.size = int(r.headers["content-length"])
        self.pos = 0
        self.calls = 0
        self.bytes = 0

    def seekable(self):
        return True

    def readable(self):
        return True

    def tell(self):
        return self.pos

    def seek(self, off, whence=0):
        self.pos = off if whence == 0 else (self.pos + off if whence == 1 else self.size + off)
        return self.pos

    def readinto(self, b):
        n = min(len(b), self.size - self.pos)
        if n <= 0:
            return 0
        a, z = self.pos, self.pos + n - 1
        for attempt in range(5):
            r = requests.get(self.url, headers={"Range": f"bytes={a}-{z}"}, timeout=120)
            if r.status_code in (200, 206) and len(r.content) == n:
                break
            time.sleep(2 ** attempt)
        else:
            raise IOError(f"range failed {r.status_code}")
        b[:n] = r.content
        self.pos += n
        self.calls += 1
        self.bytes += n
        return n


if __name__ == "__main__":
    url = sys.argv[2]
    f = RangeFile(url)
    pf = pq.ParquetFile(f)
    print("size", f.size, "rows", pf.metadata.num_rows, "row_groups", pf.metadata.num_row_groups)
    print(pf.schema_arrow)
    print("calls", f.calls, "bytes", f.bytes)
