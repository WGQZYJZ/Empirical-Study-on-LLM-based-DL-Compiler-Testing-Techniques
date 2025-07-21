'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
from torch.nn import AdaptiveMaxPool3d
import torch
input = torch.randn(1, 1, 5, 5, 5, requires_grad=True)
pool3d = AdaptiveMaxPool3d((2, 1, 1))
output = pool3d(input)
print(output)