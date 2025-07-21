'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 2, 3)
print('input_data: ', input_data)
print('torch.rad2deg: ', torch.rad2deg(input_data))