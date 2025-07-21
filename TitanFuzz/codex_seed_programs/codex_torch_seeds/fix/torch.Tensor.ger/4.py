'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ger\ntorch.Tensor.ger(_input_tensor, vec2)\n'
import torch
input_tensor = torch.rand(4, 4)
print(input_tensor)
vec2 = torch.rand(4)
print(vec2)
output_tensor = input_tensor.ger(vec2)
print(output_tensor)