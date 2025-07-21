'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
import numpy as np
import torch
in_shape = (2, 2)
out_shape = (4,)
reshape_transform = transforms.ReshapeTransform(in_shape, out_shape)
print(reshape_transform(torch.ones(in_shape)))