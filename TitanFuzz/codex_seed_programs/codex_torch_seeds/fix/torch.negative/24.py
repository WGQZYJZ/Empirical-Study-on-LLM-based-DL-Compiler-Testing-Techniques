'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.negative\ntorch.negative(input, *, out=None)\n'
import torch
input_data = torch.randn(5, 3)
print(input_data)
print(torch.negative(input_data))
print(torch.neg(input_data))