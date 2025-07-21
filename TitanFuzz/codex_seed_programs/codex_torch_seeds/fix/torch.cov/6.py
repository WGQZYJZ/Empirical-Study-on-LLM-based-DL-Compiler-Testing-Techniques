'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cov\ntorch.cov(input, *, correction=1, fweights=None, aweights=None)\n'
import torch
x = torch.randn(5, 5)
print('x: ', x)
print('Covariance of x: ', torch.cov(x))
y = torch.randn(5, 5)
print('y: ', y)
print('Covariance of y: ', torch.cov(y))