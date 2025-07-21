'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('Input Tensor :\n', input_tensor)
output = torch.Tensor.arcsin_(input_tensor)
print('Output Tensor :\n', output)
output = torch.arcsin_(input_tensor)
print('Output Tensor :\n', output)