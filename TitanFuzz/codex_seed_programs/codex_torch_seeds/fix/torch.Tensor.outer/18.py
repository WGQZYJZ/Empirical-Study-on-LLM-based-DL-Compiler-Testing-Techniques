'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
input_tensor = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
vec2 = torch.tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
torch.Tensor.outer(input_tensor, vec2)