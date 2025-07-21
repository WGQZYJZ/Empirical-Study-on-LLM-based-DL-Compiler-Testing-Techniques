'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: \n{}'.format(_input_tensor))
_output_tensor = _input_tensor.tile(3)
print('Output tensor: \n{}'.format(_output_tensor))