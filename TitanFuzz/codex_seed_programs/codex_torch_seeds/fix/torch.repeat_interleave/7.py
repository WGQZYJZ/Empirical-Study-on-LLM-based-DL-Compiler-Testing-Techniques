'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
data = torch.arange(1, 11)
print('Input data: ', data)
output = torch.repeat_interleave(data, repeats=2, dim=0)
print('Output: ', output)