'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.adaptive_avg_pool3d\ntorch.nn.functional.adaptive_avg_pool3d(input, output_size)\n'
import torch
from torch import nn
input = torch.randn(1, 1, 5, 5, 5)
output = nn.functional.adaptive_avg_pool3d(input, (3, 4, 4))
print(output)