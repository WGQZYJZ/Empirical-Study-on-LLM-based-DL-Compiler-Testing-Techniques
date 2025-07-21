'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
'\nTask 1: import PyTorch\n'
import torch
'\nTask 2: Generate input data\n'
input_tensor = torch.rand(3, 4)
vec2 = torch.rand(4)
'\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
output = torch.Tensor.outer(input_tensor, vec2)
print(output)