'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.atanh\ntorch.atanh(input, *, out=None)\n'
import torch
input_data = torch.Tensor([0.1, 0.2, 0.3, 0.4])
output = torch.atanh(input_data)
print('input:', input_data)
print('output:', output)