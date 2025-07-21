'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
input_tensor = torch.randn(3, 3)
real_tensor = torch.Tensor.real(input_tensor)
print('The real part of input_tensor is: ', real_tensor)