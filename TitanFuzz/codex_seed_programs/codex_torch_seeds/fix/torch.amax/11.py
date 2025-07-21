'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(3, 3)
print(input_data)
print(torch.amax(input_data, 0))