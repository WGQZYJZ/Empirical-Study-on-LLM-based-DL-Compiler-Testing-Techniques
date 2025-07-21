'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.view_as\ntorch.Tensor.view_as(_input_tensor, other)\n'
import torch
a = torch.arange(0, 12)
a = a.view(4, 3)
print(a)
b = torch.arange(0, 12)
b = b.view(3, 4)
print(b)
c = a.view_as(b)
print(c)