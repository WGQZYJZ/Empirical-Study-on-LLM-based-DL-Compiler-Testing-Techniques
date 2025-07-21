'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumprod\ntorch.Tensor.cumprod(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.rand(5, 5)
print(input_tensor)
print(input_tensor.cumprod(0))
print(input_tensor.cumprod(1))