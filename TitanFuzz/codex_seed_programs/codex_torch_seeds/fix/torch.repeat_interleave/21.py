'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input_data = torch.arange(12)
print('input_data = ', input_data)
output = torch.repeat_interleave(input_data, repeats=3, dim=0)
print('output = ', output)