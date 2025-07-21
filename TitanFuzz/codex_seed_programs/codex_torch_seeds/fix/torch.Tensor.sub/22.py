'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.sub\ntorch.Tensor.sub(_input_tensor, other, *, alpha=1)\n'
import torch
_input_tensor = torch.rand(3, 4)
other = torch.rand(3, 4)
_output_tensor = _input_tensor.sub(other)
print('Input tensor: ')
print(_input_tensor)
print('\nOutput tensor: ')
print(_output_tensor)