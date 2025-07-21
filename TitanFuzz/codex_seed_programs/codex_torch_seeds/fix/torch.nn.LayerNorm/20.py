'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
from torch.nn.functional import layer_norm
input_data = torch.randn(20, 5, 10)
print(input_data)
norm_layer = torch.nn.LayerNorm(input_data.size()[1:])
print(norm_layer)
output = norm_layer(input_data)
print(output)
output = layer_norm(input_data, input_data.size()[1:])
print(output)