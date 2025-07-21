'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cumsum\ntorch.cumsum(input, dim, *, dtype=None, out=None)\n'
import torch
import torch
input = torch.randn(3, 4)
print(input)
output = torch.cumsum(input, dim=1)
print(output)
output1 = torch.cumsum(input, dim=1, out=torch.empty(input.size()))
print(output1)
output2 = torch.cumsum(input, dim=1, dtype=torch.float64)
print(output2)