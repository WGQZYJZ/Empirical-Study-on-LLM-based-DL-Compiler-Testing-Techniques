'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LayerNorm\ntorch.nn.LayerNorm(normalized_shape, eps=1e-05, elementwise_affine=True, device=None, dtype=None)\n'
import torch
from torch.nn import LayerNorm
input_data = torch.randn(2, 3, 4)
print('Input data:\n', input_data)
norm = LayerNorm(input_data.size()[1:])
output = norm(input_data)
print('Output data:\n', output)