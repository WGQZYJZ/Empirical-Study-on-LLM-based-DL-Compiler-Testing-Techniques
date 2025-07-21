'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.ge\ntorch.ge(input, other, *, out=None)\n'
import torch
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
y = torch.Tensor([[1, 2, 3], [4, 5, 6]])
z = torch.ge(x, y)
print('z = ', z)