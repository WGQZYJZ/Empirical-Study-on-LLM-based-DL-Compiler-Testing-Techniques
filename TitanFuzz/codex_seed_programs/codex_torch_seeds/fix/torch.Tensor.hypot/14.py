'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot\ntorch.Tensor.hypot(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(5, 5)
other = torch.rand(5, 5)
print(torch.Tensor.hypot(input_tensor, other))
print(torch.hypot(input_tensor, other))