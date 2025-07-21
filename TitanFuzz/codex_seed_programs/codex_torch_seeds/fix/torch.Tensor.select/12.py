'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.select\ntorch.Tensor.select(_input_tensor, dim, index)\n'
import torch
input_tensor = torch.randn(5, 3)
print(input_tensor.select(1, 1))