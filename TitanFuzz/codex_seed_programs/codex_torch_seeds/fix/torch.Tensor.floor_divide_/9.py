'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(3, 3)
print('Input Tensor: \n', input_tensor)
result = torch.Tensor.floor_divide_(input_tensor, 2)
print('Result: \n', result)