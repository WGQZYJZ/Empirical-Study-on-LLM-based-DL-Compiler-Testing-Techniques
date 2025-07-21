'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.hypot\ntorch.Tensor.hypot(_input_tensor, other)\n'
import torch
input_tensor = torch.rand(5, 3)
other = torch.rand(5, 3)
hypot = input_tensor.hypot(other)
print(hypot)