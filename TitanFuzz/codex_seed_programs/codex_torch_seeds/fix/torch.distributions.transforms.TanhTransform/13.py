'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.TanhTransform\ntorch.distributions.transforms.TanhTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import TanhTransform
x = torch.randn(2, 3)
print(x)
tanh_transform = TanhTransform()
y = tanh_transform(x)
print(y)
print(tanh_transform.inv(y))
'\nTask 4: Call the API torch.distributions.transforms.AffineTransform\ntorch.distributions.transforms.AffineTransform(loc, scale, cache_size=0)\n'
affine_transform = torch.distributions.transforms.AffineTransform(loc=0.1, scale=0.2)
print(affine_transform(x))
print(affine_transform.inv(y))
'\nTask 5: Call the API torch.distributions.transforms.ComposeTransform\ntorch.distributions.transforms.ComposeTransform(parts, cache_size=0)\n'
compose_transform = torch.distributions.transforms.ComposeTransform([affine_transform, tanh_transform])