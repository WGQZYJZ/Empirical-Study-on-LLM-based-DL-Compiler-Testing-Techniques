'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.imag\ntorch.Tensor.imag(_input_tensor, )\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input tensor:', input_tensor)
imag_tensor = torch.Tensor.imag(input_tensor)
print('imag_tensor:', imag_tensor)