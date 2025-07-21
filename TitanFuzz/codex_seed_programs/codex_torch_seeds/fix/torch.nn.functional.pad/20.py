"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
from torch.nn import functional as F
input = torch.randn(1, 1, 4, 4)
print(input)
output = F.pad(input, (1, 1, 1, 1), mode='constant', value=0)
print(output)