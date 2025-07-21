'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
import torch
_input_tensor = torch.rand(2, 3)
print('Input tensor: \n{}'.format(_input_tensor))
_output_tensor = _input_tensor.double()
print('Output tensor: \n{}'.format(_output_tensor))