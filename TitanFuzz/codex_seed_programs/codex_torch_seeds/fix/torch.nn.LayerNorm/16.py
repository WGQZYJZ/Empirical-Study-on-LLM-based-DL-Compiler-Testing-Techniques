'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(64, 2, 10, 10)
norm = nn.LayerNorm([10, 10])
y = norm(x)
print(y.shape)