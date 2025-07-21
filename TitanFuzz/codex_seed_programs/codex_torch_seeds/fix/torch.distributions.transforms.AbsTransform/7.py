'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.AbsTransform\ntorch.distributions.transforms.AbsTransform(cache_size=0)\n'
import torch
import torch.distributions as dist
import torch
import torch.distributions as dist
x = torch.randn(10)
print('Input data: {}'.format(x))
abs_transform = dist.transforms.AbsTransform()
y = abs_transform(x)
print('Output data: {}'.format(y))