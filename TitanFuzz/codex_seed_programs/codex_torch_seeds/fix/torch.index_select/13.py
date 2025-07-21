'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
import torch
input_data = torch.rand(5, 3)
print('Input data: \n', input_data)
index_data = torch.tensor([1, 2])
output_data = torch.index_select(input_data, dim=0, index=index_data)
print('Output data: \n', output_data)