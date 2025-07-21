'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
from torch.nn import LayerNorm
input_data = torch.randn(20, 5, 10)
layer_norm = LayerNorm(input_data.size()[1:])
output = layer_norm(input_data)
print('input_data: ', input_data)
print('output: ', output)