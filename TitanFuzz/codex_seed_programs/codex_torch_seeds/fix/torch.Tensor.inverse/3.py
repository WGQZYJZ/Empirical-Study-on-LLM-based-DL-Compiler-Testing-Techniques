'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.inverse\ntorch.Tensor.inverse(_input_tensor)\n'
import torch
input_tensor = torch.rand(3, 3)
print('input_tensor:', input_tensor)
print('input_tensor.inverse():', input_tensor.inverse())