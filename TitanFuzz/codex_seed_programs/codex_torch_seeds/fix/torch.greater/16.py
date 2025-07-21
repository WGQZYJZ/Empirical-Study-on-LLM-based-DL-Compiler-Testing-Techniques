'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.greater\ntorch.greater(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3)
print(input_data)
print(torch.greater(input_data, 0))