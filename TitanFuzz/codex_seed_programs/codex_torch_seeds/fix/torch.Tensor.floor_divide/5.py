'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
_input_tensor = torch.rand(3, 3)
_output_tensor = torch.Tensor.floor_divide(_input_tensor, 2)
print('Input tensor:', _input_tensor)
print('Output tensor:', _output_tensor)