'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(64, 3, 32, 32)
layer_norm = nn.LayerNorm(normalized_shape=[32, 32])
output = layer_norm(x)
print(output.shape)