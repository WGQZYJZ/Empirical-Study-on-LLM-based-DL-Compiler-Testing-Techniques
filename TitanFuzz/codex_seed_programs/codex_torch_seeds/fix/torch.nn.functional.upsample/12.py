"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn.functional as F
import torch
input = torch.rand(1, 1, 4, 4)
print(input)
output = F.upsample(input, size=(10, 10), mode='bilinear')
print(output)