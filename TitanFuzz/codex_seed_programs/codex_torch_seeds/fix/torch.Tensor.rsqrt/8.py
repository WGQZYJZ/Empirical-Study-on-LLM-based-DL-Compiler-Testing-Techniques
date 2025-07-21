'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.rsqrt\ntorch.Tensor.rsqrt(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3, 3)
print('Input tensor:\n', input_tensor)
print('\nOutput tensor:\n', input_tensor.rsqrt())