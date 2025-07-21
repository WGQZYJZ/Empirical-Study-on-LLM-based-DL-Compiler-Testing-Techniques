'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.floor_divide\ntorch.floor_divide(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3, 4)
print(input_data)
floor_divide_data = torch.floor_divide(input_data, 4)
print(floor_divide_data)