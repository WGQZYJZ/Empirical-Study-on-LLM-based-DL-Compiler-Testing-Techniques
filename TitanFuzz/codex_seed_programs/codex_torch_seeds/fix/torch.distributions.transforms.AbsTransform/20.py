'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.AbsTransform\ntorch.distributions.transforms.AbsTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import AbsTransform
data = torch.tensor([(- 1), (- 2), 3, 4, (- 5)])
abs_transform = AbsTransform()
print(abs_transform(data))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.AffineTransform\ntorch.distributions.transforms.AffineTransform(loc, scale, event_dim)\n'
import torch
from torch.distributions.transforms import AffineTransform
data = torch.tensor([[(- 1), (- 2), 3, 4, (- 5)], [(- 6), 7, 8, (- 9), 10]])
affine_transform = AffineTransform(loc=0.5, scale=2.0, event_dim=0)
print(affine_transform(data))