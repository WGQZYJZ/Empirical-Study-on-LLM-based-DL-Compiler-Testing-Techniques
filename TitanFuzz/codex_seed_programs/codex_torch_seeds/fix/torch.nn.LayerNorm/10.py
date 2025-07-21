'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(2, 3, 4)
layer_norm = torch.nn.LayerNorm(input_data.size()[1:])
output = layer_norm(input_data)
print('layer_norm: ', layer_norm)
print('output: ', output)