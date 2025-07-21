'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
input_data = torch.randn(5, 5)
other_data = torch.tensor([2, 2, 2, 2, 2])
output = torch.ldexp(input_data, other_data)
print('output = ', output)