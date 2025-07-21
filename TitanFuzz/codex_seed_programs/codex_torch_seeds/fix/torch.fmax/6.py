'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fmax\ntorch.fmax(input, other, *, out=None)\n'
import torch
input_data = torch.randn(2, 3)
other_data = torch.randn(2, 3)
output = torch.fmax(input_data, other_data)
print('output = ', output)