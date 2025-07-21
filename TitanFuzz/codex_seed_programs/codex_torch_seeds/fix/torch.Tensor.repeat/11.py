'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.repeat\ntorch.Tensor.repeat(_input_tensor, *sizes)\n'
import torch
_input_tensor = torch.randn(2, 3)
_output_tensor = _input_tensor.repeat(2, 2)
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)