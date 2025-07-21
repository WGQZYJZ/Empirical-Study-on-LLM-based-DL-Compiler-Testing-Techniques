'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 5, 5)
print('Input: ', input)
print('Input shape: ', input.shape)
output = F.upsample_nearest(input, size=(10, 10))
print('Output: ', output)
print('Output shape: ', output.shape)