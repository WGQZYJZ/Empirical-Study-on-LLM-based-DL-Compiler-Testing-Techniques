'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ldexp\ntorch.ldexp(input, other, *, out=None)\n'
import torch
input_data = torch.arange(1, 10, dtype=torch.float)
other_data = torch.arange(1, 10, dtype=torch.float)
output = torch.ldexp(input_data, other_data)
print('Output = ', output)