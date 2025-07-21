'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.addmv_\ntorch.Tensor.addmv_(_input_tensor, mat, vec, *, beta=1, alpha=1)\n'
import torch
import numpy as np
input_tensor = torch.randn(2, 3)
mat = torch.randn(3, 4)
vec = torch.randn(4)
print(input_tensor)
print(mat)
print(vec)
input_tensor.addmv_(mat, vec, alpha=0.5, beta=0.5)
print(input_tensor)