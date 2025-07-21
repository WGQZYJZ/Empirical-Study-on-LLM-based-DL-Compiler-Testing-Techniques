'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.acos\ntorch.acos(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(torch.acos(input_data))