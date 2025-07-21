'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lerp\ntorch.lerp(input, end, weight, *, out=None)\n'
import torch
a = torch.randn(4, 4)
b = torch.randn(4, 4)
weight = torch.tensor([[0.1, 0.2, 0.3, 0.4], [0.5, 0.6, 0.7, 0.8], [0.9, 1.0, 1.1, 1.2], [1.3, 1.4, 1.5, 1.6]])
print('weight = ', weight)
print('a = ', a)
print('b = ', b)
print('\nResult of torch.lerp(a, b, weight) = ', torch.lerp(a, b, weight))