'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
from torch.distributions.transforms import ReshapeTransform
in_shape = torch.Size([2, 2])
out_shape = torch.Size([4])
reshape_transform = ReshapeTransform(in_shape, out_shape)
print('Input shape: ', in_shape)
print('Output shape: ', out_shape)
print('ReshapeTransform: ', reshape_transform)