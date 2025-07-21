'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view\ntorch.Tensor.view(_input_tensor, *shape)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: {}'.format(_input_tensor))
_output_tensor = _input_tensor.view(3, 2)
print('Output tensor: {}'.format(_output_tensor))