'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.normalize\ntorch.nn.functional.normalize(input, p=2.0, dim=1, eps=1e-12, out=None)\n'
import torch
import torch.nn.functional as F
input = torch.randn(3, 5)
print(input)
output = F.normalize(input, p=2, dim=1)
print(output)
output = torch.empty(3, 5)
F.normalize(input, p=2, dim=1, out=output)
print(output)
output = F.normalize(input, p=2, dim=1, eps=1e-12)
print(output)