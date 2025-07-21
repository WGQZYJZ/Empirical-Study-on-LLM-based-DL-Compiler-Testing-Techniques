'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.index_select\ntorch.index_select(input, dim, index, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print('input_data: ', input_data)
index_data = torch.tensor([0, 2])
print('index_data: ', index_data)
output_data = torch.index_select(input_data, dim=0, index=index_data)
print('output_data: ', output_data)