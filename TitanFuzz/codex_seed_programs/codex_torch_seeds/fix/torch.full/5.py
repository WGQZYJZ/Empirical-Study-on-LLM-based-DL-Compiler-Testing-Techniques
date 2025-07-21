'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.full\ntorch.full(size, fill_value, *, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.full')
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]])
print('input_data = \n', input_data)
output_data = torch.full(input_data.shape, fill_value=10, dtype=torch.int32)
print('output_data = \n', output_data)