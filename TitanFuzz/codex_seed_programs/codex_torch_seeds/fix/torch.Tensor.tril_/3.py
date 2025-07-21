'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tril_\ntorch.Tensor.tril_(_input_tensor, diagonal=0)\n'
import torch
input_tensor = torch.randn(3, 3)
print('Input tensor:', input_tensor)
output_tensor = input_tensor.tril_()
print('Output tensor:', output_tensor)