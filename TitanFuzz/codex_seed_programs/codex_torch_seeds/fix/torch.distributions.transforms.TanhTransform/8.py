'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.TanhTransform\ntorch.distributions.transforms.TanhTransform(cache_size=0)\n'
import torch
import torch.distributions as dist
x = torch.randn(4, 4)
print('Input data: ', x)
tanh_transform = dist.transforms.TanhTransform(cache_size=0)
print('Output data: ', tanh_transform(x))