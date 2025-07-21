'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pdist\ntorch.nn.functional.pdist(input, p=2)\n'
import torch
import torch.nn.functional as F
input = torch.randn(10, 3)
output = F.pdist(input)
print(input)
print(output)