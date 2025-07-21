'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.any\ntorch.any(input, dim, keepdim=False, *, out=None)\n'
import torch
x = torch.randn(2, 3)
print(x)
output = torch.any((x > 0))
print(output)
output = torch.any((x > 0), dim=0)
print(output)
output = torch.any((x > 0), dim=1)
print(output)
output = torch.any((x > 0), dim=1, keepdim=True)
print(output)