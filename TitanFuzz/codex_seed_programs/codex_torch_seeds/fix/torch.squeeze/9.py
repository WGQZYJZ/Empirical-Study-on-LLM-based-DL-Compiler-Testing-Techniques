'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.squeeze\ntorch.squeeze(input, dim=None, *, out=None)\n'
import torch
a = torch.randn(1, 2, 1, 3, 1)
print(a.size())
b = torch.squeeze(a, dim=0)
print(b.size())
c = torch.squeeze(a, dim=1)
print(c.size())
d = torch.squeeze(a, dim=2)
print(d.size())
e = torch.squeeze(a, dim=3)
print(e.size())
f = torch.squeeze(a, dim=4)
print(f.size())