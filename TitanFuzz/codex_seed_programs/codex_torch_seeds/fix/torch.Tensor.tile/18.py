'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.tile\ntorch.Tensor.tile(_input_tensor, dims)\n'
import torch
_input_tensor = torch.rand(3, 3)
print('Input tensor:')
print(_input_tensor)
print()
_output_tensor = _input_tensor.tile(2)
print('Output tensor:')
print(_output_tensor)