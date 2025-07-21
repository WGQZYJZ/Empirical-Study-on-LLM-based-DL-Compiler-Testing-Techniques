'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.randn_like\ntorch.randn_like(input, *, dtype=None, layout=None, device=None, requires_grad=False, memory_format=torch.preserve_format)\n'
import torch
x = torch.ones(5, 3, dtype=torch.double)
print(x)
print(x.size())
y = torch.randn_like(x, dtype=torch.float)
print(y)
print(y.size())
z = torch.randn_like(x, dtype=torch.double)
print(z)
print(z.size())