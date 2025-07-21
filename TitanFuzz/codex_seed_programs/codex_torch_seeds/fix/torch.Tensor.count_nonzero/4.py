'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.count_nonzero\ntorch.Tensor.count_nonzero(_input_tensor, dim=None)\n'
import torch
_input_tensor = torch.randn(4, 4)
print('Input tensor is: \n{}\n'.format(_input_tensor))
_output_tensor = _input_tensor.count_nonzero()
print('Output tensor is: \n{}\n'.format(_output_tensor))
_output_tensor = _input_tensor.count_nonzero(dim=0)
print('Output tensor is: \n{}\n'.format(_output_tensor))
_output_tensor = _input_tensor.count_nonzero(dim=1)
print('Output tensor is: \n{}\n'.format(_output_tensor))