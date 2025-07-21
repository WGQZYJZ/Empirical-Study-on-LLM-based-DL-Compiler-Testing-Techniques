'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input = torch.randn(3, 3)
print('Input data: ')
print(_input)
_input_tensor = torch.Tensor.double(_input)
print('Output data: ')
print(_input_tensor)