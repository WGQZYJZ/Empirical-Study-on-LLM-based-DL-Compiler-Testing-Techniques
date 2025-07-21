'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
import torch.nn.functional as F
input = torch.randn(1, 1, 2, 2)
output = F.upsample_bilinear(input, scale_factor=2)
print('input size: ', input.size())
print('output size: ', output.size())