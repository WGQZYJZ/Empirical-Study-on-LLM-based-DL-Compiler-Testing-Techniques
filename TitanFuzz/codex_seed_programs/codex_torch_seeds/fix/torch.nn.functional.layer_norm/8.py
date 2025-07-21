'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.layer_norm\ntorch.nn.functional.layer_norm(input, normalized_shape, weight=None, bias=None, eps=1e-05)\n'
import torch
from torch.nn import functional as F
input = torch.randn(3, 4, 5, 6)
normalized_shape = [4, 5, 6]
weight = torch.randn(4, 5, 6)
bias = torch.randn(4, 5, 6)
eps = 1e-05
output = F.layer_norm(input, normalized_shape, weight, bias, eps)
print(output)