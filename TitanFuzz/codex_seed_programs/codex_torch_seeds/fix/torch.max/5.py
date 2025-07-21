'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.max\ntorch.max(input, dim, keepdim=False, *, out=None)\n'
import torch
input_data = torch.rand(3, 4)
print(input_data)
print(torch.max(input_data, dim=1))
print(torch.max(input_data, dim=1, keepdim=True))
print(torch.max(input_data, dim=1, keepdim=True)[0])
print(torch.max(input_data, dim=1, keepdim=True)[1])