'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.imag\ntorch.Tensor.imag(_input_tensor, )\n'
import torch
input_tensor = torch.randn(4, 4)
output_tensor = torch.Tensor.imag(input_tensor)
print('input tensor: ', input_tensor)
print('output tensor: ', output_tensor)