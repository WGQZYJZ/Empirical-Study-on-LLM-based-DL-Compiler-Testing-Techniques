'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.hypot\ntorch.hypot(input, other, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
other_data = torch.randn(5, 5)
print(torch.hypot(input_data, other_data))
print(torch.hypot(input_data, other_data).size())