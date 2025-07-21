'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
_input_tensor = torch.randn(2, 3)
print('Input tensor:\n', _input_tensor)
print('Output tensor:\n', torch.Tensor.floor_divide(_input_tensor, 2))