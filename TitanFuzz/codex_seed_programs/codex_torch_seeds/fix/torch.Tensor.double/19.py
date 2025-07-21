'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.double\ntorch.Tensor.double(_input_tensor, memory_format=torch.preserve_format)\n'
import torch
_input_tensor = torch.rand(2, 3, 4, 5)
_double_tensor = torch.Tensor.double(_input_tensor)
print('_input_tensor: {}'.format(_input_tensor))
print('_double_tensor: {}'.format(_double_tensor))