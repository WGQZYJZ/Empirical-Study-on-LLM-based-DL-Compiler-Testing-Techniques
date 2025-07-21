'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
_input_tensor = torch.randn(2, 3)
other = torch.randn(2, 3)
output_tensor = torch.Tensor.add(_input_tensor, other)
print('Input tensor: ', _input_tensor)
print('Other tensor: ', other)
print('Output tensor: ', output_tensor)