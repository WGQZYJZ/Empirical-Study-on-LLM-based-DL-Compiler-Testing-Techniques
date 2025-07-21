'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.square\ntorch.Tensor.square(_input_tensor)\n'
import torch
_input_tensor = torch.rand(3, 4)
print('Input Tensor:')
print(_input_tensor)
_output_tensor = torch.Tensor.square(_input_tensor)
print('Output Tensor:')
print(_output_tensor)