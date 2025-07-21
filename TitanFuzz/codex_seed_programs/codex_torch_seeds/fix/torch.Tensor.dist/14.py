'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.dist\ntorch.Tensor.dist(_input_tensor, other, p=2)\n'
import torch
input_tensor = torch.rand(2, 3)
other = torch.rand(2, 3)
print(input_tensor.dist(other, p=2))