'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lt\ntorch.Tensor.lt(_input_tensor, other)\n'
import torch
a = torch.rand(3, 3)
b = torch.rand(3, 3)
print(a)
print(b)
print(a.lt(b))