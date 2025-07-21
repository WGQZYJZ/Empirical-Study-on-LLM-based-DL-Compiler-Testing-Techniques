'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.eq\ntorch.eq(input, other, *, out=None)\n'
import torch
input_data = torch.randn(10, 10)
other_data = torch.randn(10, 10)
output = torch.eq(input_data, other_data)
print(output)