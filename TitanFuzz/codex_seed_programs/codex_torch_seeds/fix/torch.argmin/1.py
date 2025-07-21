'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.argmin\ntorch.argmin(input, dim=None, keepdim=False)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
print(torch.argmin(input_data, dim=1))