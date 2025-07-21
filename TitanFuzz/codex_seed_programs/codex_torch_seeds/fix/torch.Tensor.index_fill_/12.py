'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(2, 3, 4)
print('Input tensor:', input_tensor)
dim = 1
index = torch.LongTensor([0, 2])
value = 0.0
output_tensor = torch.Tensor().index_fill_(input_tensor, dim, index, value)
print('Output tensor:', output_tensor)