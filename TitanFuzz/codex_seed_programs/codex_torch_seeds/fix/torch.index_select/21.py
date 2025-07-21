'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input_data = torch.arange(0, 12).view(3, 4)
print('input data: ', input_data)
index_data = torch.tensor([0, 2])
output_data = torch.index_select(input_data, 0, index_data)
print('output data: ', output_data)