'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input = torch.randn(20, 5, 10, 10)
m = nn.LayerNorm(input.size()[1:])
output = m(input)
print(output.size())