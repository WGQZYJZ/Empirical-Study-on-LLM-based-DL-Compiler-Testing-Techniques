'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(5, 3, 2)
layer_norm = nn.LayerNorm(2)
output = layer_norm(input_data)
print(output)