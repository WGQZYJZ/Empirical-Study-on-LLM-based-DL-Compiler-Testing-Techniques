'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.diff\ntorch.Tensor.diff(_input_tensor, n=1, dim=-1, prepend=None, append=None)\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = torch.Tensor.diff(_input_tensor, n=1, dim=(- 1), prepend=None, append=None)
print('Input Tensor: ', _input_tensor)
print('Output Tensor: ', _output_tensor)