'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.subtract_\ntorch.Tensor.subtract_(_input_tensor, other, *, alpha=1)\n'
import torch
import numpy as np
x = torch.randn(4, 4)
y = torch.randn(4, 4)
z = torch.Tensor.subtract_(x, y)
print(z)
z = torch.Tensor.subtract_(x, y, alpha=2)
print(z)
z = torch.Tensor.subtract_(x, y, alpha=3)
print(z)