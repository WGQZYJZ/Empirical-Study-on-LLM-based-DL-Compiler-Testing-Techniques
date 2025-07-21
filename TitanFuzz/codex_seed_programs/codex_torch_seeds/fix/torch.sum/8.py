'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
print(torch.__version__)
a = torch.ones(3, 3)
b = torch.ones(3, 3)
c = torch.sum((a + b))
print(c)
'\nTask 4: Call the API torch.mean\ntorch.mean(input, dim, keepdim=False, *, out=None)\n'
d = torch.mean((a + b))
print(d)
'\nTask 5: Call the API torch.max\ntorch.max(input, dim, keepdim=False, out=None)\n'
e = torch.max((a + b))
print(e)
'\nTask 6: Call the API torch.min\ntorch.min(input, dim, keepdim=False, out=None)\n'
f = torch.min((a + b))
print(f)