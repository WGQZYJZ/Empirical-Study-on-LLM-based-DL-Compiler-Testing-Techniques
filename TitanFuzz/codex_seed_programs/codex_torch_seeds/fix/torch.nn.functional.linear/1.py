'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.linear\ntorch.nn.functional.linear(input, weight, bias=None)\n'
import torch
import torch.nn.functional as F
import torch
input = torch.randn(2, 3)
weight = torch.randn(4, 3)
output = F.linear(input, weight)
print(output)
output = F.linear(input, weight, bias=torch.randn(4))
print(output)