'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.real\ntorch.Tensor.real(_input_tensor, )\n'
import torch
_input_tensor = torch.randn(3, 3)
_output_tensor = _input_tensor.real()
print('input:', _input_tensor)
print('output:', _output_tensor)