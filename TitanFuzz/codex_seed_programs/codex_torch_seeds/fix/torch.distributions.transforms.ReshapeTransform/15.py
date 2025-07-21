'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
from torch.distributions import transforms
import torch
x = torch.randn(2, 3, 4)
reshape = transforms.ReshapeTransform(in_shape=(2, 3, 4), out_shape=(3, 8))
reshape(x)