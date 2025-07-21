'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.rad2deg\ntorch.rad2deg(input, *, out=None)\n'
import torch
input_data = torch.rand(1, requires_grad=True)
print(input_data)
print(torch.rad2deg(input_data))