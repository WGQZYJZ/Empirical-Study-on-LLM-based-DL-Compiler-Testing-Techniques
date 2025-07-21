'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.transpose_\ntorch.Tensor.transpose_(_input_tensor, dim0, dim1)\n'
import torch
input_tensor = torch.randn(2, 3, 5)
print('Input tensor: ', input_tensor)
output_tensor = torch.Tensor.transpose_(input_tensor, 0, 2)
print('Output tensor: ', output_tensor)