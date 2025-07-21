'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cummax\ntorch.Tensor.cummax(_input_tensor, dim)\n'
import torch
_input_tensor = torch.rand(2, 3)
print('Input Tensor:')
print(_input_tensor)
_output_tensor = _input_tensor.cummax(dim=1)
print('Output Tensor:')
print(_output_tensor)