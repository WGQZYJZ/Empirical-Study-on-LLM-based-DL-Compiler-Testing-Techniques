'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cosh_\ntorch.Tensor.cosh_(_input_tensor)\n'
import torch
input_tensor = torch.randn(1, 3, 3)
print('Input Tensor :\n', input_tensor)
torch.Tensor.cosh_(input_tensor)
print('Output Tensor :\n', input_tensor)