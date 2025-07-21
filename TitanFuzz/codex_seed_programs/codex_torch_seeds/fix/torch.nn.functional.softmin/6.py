'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softmin\ntorch.nn.functional.softmin(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
y = torch.nn.functional.softmin(x, dim=0)
print(y)