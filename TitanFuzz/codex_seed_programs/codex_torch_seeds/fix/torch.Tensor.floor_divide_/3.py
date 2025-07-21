'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide_\ntorch.Tensor.floor_divide_(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[2, 4, 6], [8, 10, 12]])
print('Input tensor: ', input_tensor)
input_tensor = torch.tensor([[2, 4, 6], [8, 10, 12]])
print('Input tensor: ', input_tensor)
print('Output tensor: ', input_tensor.floor_divide_(2))