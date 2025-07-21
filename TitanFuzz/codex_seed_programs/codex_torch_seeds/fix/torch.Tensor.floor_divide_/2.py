'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.rand(2, 2)
print('Input Tensor: ', input_tensor)
print('Output Tensor: ', input_tensor.floor_divide_(2))