'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add_\ntorch.Tensor.add_(_input_tensor, other, *, alpha=1)\n'
import torch
input_tensor = torch.randn(2, 3)
other = torch.randn(3)
output_tensor = torch.Tensor.add_(input_tensor, other)
print('Input tensor:\n', input_tensor)
print('Other tensor:\n', other)
print('Output tensor:\n', output_tensor)