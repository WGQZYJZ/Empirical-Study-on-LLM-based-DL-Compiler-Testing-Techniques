'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.reciprocal\ntorch.Tensor.reciprocal(_input_tensor)\n'
import torch
_input_tensor = torch.randn(3, 3)
print('Input Tensor: \n', _input_tensor)
_output_tensor = torch.Tensor.reciprocal(_input_tensor)
print('Output Tensor: \n', _output_tensor)