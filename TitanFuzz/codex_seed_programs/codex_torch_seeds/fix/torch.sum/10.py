'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input = torch.randn(4, 3)
print(input)
sum_result = torch.sum(input, dim=1)
print(sum_result)
sum_result = torch.sum(input, dim=1, keepdim=True)
print(sum_result)
sum_result = torch.sum(input, dim=1, keepdim=False)
print(sum_result)