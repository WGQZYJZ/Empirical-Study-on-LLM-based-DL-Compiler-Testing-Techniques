'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.cumsum\ntorch.Tensor.cumsum(_input_tensor, dim, dtype=None)\n'
import torch
input_tensor = torch.rand(3, 3)
print(input_tensor)
print(input_tensor.cumsum(0))
print(input_tensor.cumsum(1))
print(input_tensor.cumsum(1, dtype=torch.float32))