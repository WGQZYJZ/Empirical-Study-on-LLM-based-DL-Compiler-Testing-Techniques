'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sum\ntorch.sum(input, dim, keepdim=False, *, dtype=None)\n'
import torch
input_data = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
sum_result = torch.sum(input=input_data, dim=0)
print('input_data: \n', input_data)
print('sum_result: \n', sum_result)