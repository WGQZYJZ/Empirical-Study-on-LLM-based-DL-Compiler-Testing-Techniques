'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.outer\ntorch.Tensor.outer(_input_tensor, vec2)\n'
import torch
import numpy as np
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
vec2 = torch.tensor([1, 2, 3])
output_tensor = torch.Tensor.outer(input_tensor, vec2)
print(output_tensor)