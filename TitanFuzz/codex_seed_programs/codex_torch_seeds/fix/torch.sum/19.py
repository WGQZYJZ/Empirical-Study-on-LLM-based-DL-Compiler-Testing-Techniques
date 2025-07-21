'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input_data = torch.rand(2, 3)
print(input_data)
sum_result = torch.sum(input_data, dim=1)
print(sum_result)
sum_result = torch.sum(input_data, dim=1, keepdim=True)
print(sum_result)
sum_result = torch.sum(input_data, dim=0)
print(sum_result)
sum_result = torch.sum(input_data, dim=0, keepdim=True)
print(sum_result)