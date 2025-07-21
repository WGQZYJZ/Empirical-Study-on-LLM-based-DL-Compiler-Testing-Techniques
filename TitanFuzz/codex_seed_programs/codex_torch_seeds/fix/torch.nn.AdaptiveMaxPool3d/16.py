'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AdaptiveMaxPool3d\ntorch.nn.AdaptiveMaxPool3d(output_size, return_indices=False)\n'
import torch
from torch.nn import AdaptiveMaxPool3d
input = torch.randn(1, 2, 3, 4, 5)
output = AdaptiveMaxPool3d(output_size=(3, 4, 5))(input)
print('input: ', input)
print('output: ', output)