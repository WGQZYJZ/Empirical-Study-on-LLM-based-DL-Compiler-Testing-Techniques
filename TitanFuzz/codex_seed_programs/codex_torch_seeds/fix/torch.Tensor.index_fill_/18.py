'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.index_fill_\ntorch.Tensor.index_fill_(_input_tensor, dim, index, value)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input Tensor: ', input_tensor)
index = torch.tensor([0, 2])
output_tensor = input_tensor.index_fill_(1, index, 0)
print('Output Tensor: ', output_tensor)