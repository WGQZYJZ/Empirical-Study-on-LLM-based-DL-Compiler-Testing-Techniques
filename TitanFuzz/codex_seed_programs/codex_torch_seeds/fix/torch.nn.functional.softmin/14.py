'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softmin\ntorch.nn.functional.softmin(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
x = torch.randn(3, requires_grad=True)
y = torch.nn.functional.softmin(x, dim=0)
print(x)
print(y)
z = torch.nn.Softmin(dim=0)
print(z(x))