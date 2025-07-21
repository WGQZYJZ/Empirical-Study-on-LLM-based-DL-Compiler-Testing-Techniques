'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.remainder_\ntorch.Tensor.remainder_(_input_tensor, divisor)\n'
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor = ', input_tensor)
import torch
input_tensor = torch.randn(2, 3)
print('input_tensor = ', input_tensor)
output_tensor = torch.Tensor.remainder_(input_tensor, 2)
print('output_tensor = ', output_tensor)