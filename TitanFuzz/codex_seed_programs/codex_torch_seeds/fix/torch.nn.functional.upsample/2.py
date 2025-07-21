"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn.functional as F
import torch
input = torch.randn(1, 1, 4, 4)
print('input: ', input)
output = F.upsample(input, size=(8, 8), mode='nearest')
print('output: ', output)
print('output: ', output)