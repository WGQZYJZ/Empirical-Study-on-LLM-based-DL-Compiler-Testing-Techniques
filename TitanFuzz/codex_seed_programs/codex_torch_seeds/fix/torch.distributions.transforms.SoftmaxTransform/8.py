'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SoftmaxTransform\ntorch.distributions.transforms.SoftmaxTransform(cache_size=0)\n'
import torch
import torch.distributions
from torch.distributions import transforms
x = torch.randn(10, 5)
print('x: ', x)
softmax_transform = transforms.SoftmaxTransform(cache_size=0)
print('softmax_transform: ', softmax_transform)
y = softmax_transform(x)
print('y: ', y)
print('y.sum(dim=-1): ', y.sum(dim=(- 1)))