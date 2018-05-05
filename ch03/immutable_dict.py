from types import MappingProxyType

d = {1: "A"}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
try:
    d_proxy[2] = 'X'
except:
    print("Error")

d[2] = 'B'
print(d_proxy)