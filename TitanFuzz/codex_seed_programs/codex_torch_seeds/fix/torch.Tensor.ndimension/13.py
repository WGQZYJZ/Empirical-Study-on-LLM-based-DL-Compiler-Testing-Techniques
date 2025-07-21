'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ndimension\ntorch.Tensor.ndimension(_input_tensor)\n'
import torch
_input_tensor = torch.randn(4, 3)
print('Input Tensor: ')
print(_input_tensor)
print('Output: ')
print(torch.Tensor.ndimension(_input_tensor))