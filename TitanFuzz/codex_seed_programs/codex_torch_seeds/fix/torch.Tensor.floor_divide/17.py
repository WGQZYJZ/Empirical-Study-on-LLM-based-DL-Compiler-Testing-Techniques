'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.floor_divide\ntorch.Tensor.floor_divide(_input_tensor, value)\n'
import torch
input_tensor = torch.tensor([[1, 2], [3, 4]])
print('Input tensor: ', input_tensor)
floor_divide_tensor = torch.Tensor.floor_divide(input_tensor, 2)
print('floor_divide_tensor: ', floor_divide_tensor)