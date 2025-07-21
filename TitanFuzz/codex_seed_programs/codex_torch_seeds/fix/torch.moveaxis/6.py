'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.moveaxis\ntorch.moveaxis(input, source, destination)\n'
import torch
x = torch.randn(3, 4, 5)
print('x: ', x)
print('x.shape: ', x.shape)
y = torch.moveaxis(x, 2, 0)
print('y: ', y)
print('y.shape: ', y.shape)
z = torch.moveaxis(x, 1, (- 1))
print('z: ', z)
print('z.shape: ', z.shape)
a = torch.moveaxis(x, (- 1), 2)
print('a: ', a)
print('a.shape: ', a.shape)