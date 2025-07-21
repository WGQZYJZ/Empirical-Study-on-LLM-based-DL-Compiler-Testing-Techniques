'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.less_\ntorch.Tensor.less_(_input_tensor, other)\n'
import torch
_input_tensor = torch.tensor([(- 1), 0, 1])
_output_tensor = _input_tensor.less_(0)
print('Input tensor: {}'.format(_input_tensor))
print('Output tensor: {}'.format(_output_tensor))