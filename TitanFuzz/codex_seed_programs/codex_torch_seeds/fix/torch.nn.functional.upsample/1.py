"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn.functional as F
x = torch.randn(1, 1, 3, 3)
print(x)
y = F.upsample(x, size=None, scale_factor=2, mode='nearest')
print(y)