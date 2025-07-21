'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.repeat_interleave\ntorch.repeat_interleave(input, repeats, dim=None)\n'
import torch
input = torch.arange(1, 4, dtype=torch.float32)
print('Input: ', input)
repeats = 3
output = torch.repeat_interleave(input, repeats, dim=0)
print('Output: ', output)