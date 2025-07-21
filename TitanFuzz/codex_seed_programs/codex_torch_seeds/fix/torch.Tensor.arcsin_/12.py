'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.arcsin_\ntorch.Tensor.arcsin_(_input_tensor)\n'
import torch
import math
a = torch.randn(1, 3)
print(a)
print(a.size())
print(type(a))
print(a.dtype)
torch.Tensor.arcsin_(a)
print(a)
print(a.size())
print(type(a))
print(a.dtype)