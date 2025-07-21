'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ger\ntorch.Tensor.ger(_input_tensor, vec2)\n'
import torch
input_tensor = torch.rand(2, 3)
vec2 = torch.rand(3)
output_tensor = torch.Tensor.ger(input_tensor, vec2)
print(output_tensor)