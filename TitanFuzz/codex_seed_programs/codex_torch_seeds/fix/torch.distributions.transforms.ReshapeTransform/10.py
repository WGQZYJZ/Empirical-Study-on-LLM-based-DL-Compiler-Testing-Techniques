'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
from torch.distributions.transforms import ReshapeTransform
in_shape = [1, 2, 3]
out_shape = [3, 2, 1]
reshape_transform = ReshapeTransform(in_shape, out_shape)
print(reshape_transform)