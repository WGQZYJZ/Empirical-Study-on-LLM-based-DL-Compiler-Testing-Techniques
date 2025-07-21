'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.add\ntorch.Tensor.add(_input_tensor, other, *, alpha=1)\n'
import torch
x = torch.rand(3, 3)
y = torch.rand(3, 3)
print(x)
print(y)
print(x.add(y))
print(x.add_(y))
print(x)