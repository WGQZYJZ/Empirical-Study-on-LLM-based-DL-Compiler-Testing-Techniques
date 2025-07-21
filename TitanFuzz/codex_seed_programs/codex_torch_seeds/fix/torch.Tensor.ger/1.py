'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.ger\ntorch.Tensor.ger(_input_tensor, vec2)\n'
import torch
input_tensor = torch.randn(3, 3)
vec2 = torch.randn(3)
torch.Tensor.ger(input_tensor, vec2)