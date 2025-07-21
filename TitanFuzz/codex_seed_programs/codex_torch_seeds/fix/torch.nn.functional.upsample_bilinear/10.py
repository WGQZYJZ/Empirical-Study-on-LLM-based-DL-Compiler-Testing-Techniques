'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
import torch.nn.functional as F
import numpy as np
input = torch.randn(1, 1, 3, 3)
print(input)
output = F.upsample_bilinear(input, size=None, scale_factor=2)
print(output)