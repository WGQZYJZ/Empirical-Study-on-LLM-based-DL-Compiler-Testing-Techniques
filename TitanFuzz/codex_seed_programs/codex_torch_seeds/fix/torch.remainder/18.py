'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
print(input_data)
remainder_data = torch.remainder(input_data, 2)
print(remainder_data)
print(remainder_data.size())