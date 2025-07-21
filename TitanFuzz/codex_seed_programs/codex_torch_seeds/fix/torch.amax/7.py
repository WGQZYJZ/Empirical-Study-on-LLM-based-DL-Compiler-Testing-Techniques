'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.amax\ntorch.amax(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
print(input_data)
print(torch.amax(input_data))
print(torch.amax(input_data, dim=0))
print(torch.amax(input_data, dim=1))
print(torch.amax(input_data, dim=0, keepdim=True))
print(torch.amax(input_data, dim=1, keepdim=True))