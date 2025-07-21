'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor: \n', input_tensor)
output_tensor = torch.Tensor.tril_(input_tensor, diagonal=0)
print('Output Tensor: \n', output_tensor)