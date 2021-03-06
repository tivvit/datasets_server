from storage.lmdbStorage import LmdbStorage
from conf import Cfg
from datasets import Datasets

cfg = Cfg()
s = LmdbStorage(cfg)
d = Datasets(cfg, s)

# print(d.generate())
# print("*" * 50)

d.scan(["data"])

s.load()
print("*" * 50)

# print(s.data)
# s.delete("8b88a424-dbd8-4032-8be7-a930a415b9a5")
# d.use("8b88a424-dbd8-4032-8be7-a930a415b9a5", {"user": "aaa", "op": "a"})

