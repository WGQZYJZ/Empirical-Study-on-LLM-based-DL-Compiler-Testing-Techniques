'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
import numpy as np
from torch.distributions.transforms import ReshapeTransform
x = torch.randn(2, 3, 4)
print('Input tensor x: ', x)
reshape_transform = ReshapeTransform((2, 3, 4), (3, 8))
y = reshape_transform(x)
print('Output tensor y: ', y)