'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
input_tensor = torch.randn(2, 3)
vec2 = torch.randn(3)
print('input_tensor:', input_tensor)
print('vec2:', vec2)
output_tensor = input_tensor.outer(vec2)
print('output_tensor:', output_tensor)