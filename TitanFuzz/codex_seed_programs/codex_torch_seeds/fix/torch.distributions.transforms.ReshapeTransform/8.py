'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
data = torch.rand(3, 4, 5)
print('Input data:', data)
reshape_transform = transforms.ReshapeTransform(in_shape=(3, 4, 5), out_shape=(5, 12))
reshape_data = reshape_transform(data)
print('Transformed data:', reshape_data)