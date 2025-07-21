'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.nn.functional import upsample_nearest
import torch
input = torch.rand(1, 2, 3, 4)
output = upsample_nearest(input, scale_factor=2)
print('input: ', input)
print('output: ', output)