'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
import torch.distributions as dist
in_shape = [2, 3, 4]
out_shape = [2, 4, 3]
reshape_transform = dist.transforms.ReshapeTransform(in_shape, out_shape)