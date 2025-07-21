'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.round\ntorch.round(input, *, out=None)\n'
import torch
input_data = torch.rand(1, 2, 3)
print(input_data)
print(torch.round(input_data))