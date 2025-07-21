'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.greater_equal\ntorch.Tensor.greater_equal(_input_tensor, other)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input tensor:', _input_tensor)
_output_tensor = torch.Tensor.greater_equal(_input_tensor, 0)
print('Output tensor:', _output_tensor)
_output_tensor = torch.ge(_input_tensor, 0)
print('Output tensor:', _output_tensor)