'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill\ntorch.Tensor.index_fill(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(4, 4)
print('Input tensor: ', input_tensor)
dim = 0
index = torch.tensor([0, 2])
value = 0
output_tensor = input_tensor.index_fill(dim, index, value)
print('Output tensor: ', output_tensor)