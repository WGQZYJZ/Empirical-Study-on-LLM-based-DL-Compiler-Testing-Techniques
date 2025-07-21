'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.lt\ntorch.Tensor.lt(_input_tensor, other)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
print(a)
print(b)
print(a.lt(b))