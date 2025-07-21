'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
from torch.distributions.transforms import ReshapeTransform
input_data = torch.randn(3, 4, 5)
print('Input data:\n', input_data)
reshape_transform = ReshapeTransform((3, 4, 5), (5, 12))
print('Reshape transform:', reshape_transform)
output = reshape_transform(input_data)
print('Output:\n', output)