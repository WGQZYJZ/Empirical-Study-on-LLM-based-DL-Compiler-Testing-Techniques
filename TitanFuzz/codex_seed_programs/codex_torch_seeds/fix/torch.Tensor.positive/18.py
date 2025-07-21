'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.positive\ntorch.Tensor.positive(_input_tensor)\n'
import torch
_input_tensor = torch.randn(10)
_output_tensor = _input_tensor.positive()
print('Input tensor:')
print(_input_tensor)
print('Output tensor:')
print(_output_tensor)