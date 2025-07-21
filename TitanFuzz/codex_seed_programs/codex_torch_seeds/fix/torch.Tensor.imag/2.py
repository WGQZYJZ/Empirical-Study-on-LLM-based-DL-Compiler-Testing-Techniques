'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.imag\ntorch.Tensor.imag(_input_tensor, )\n'
import torch
input_tensor = torch.randn(1, 3, 3)
imag_tensor = torch.Tensor.imag(input_tensor)
print(input_tensor)
print(imag_tensor)