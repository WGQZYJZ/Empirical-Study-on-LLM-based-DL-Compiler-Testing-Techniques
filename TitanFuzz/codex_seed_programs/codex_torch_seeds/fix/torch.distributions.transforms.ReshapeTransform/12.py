'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
import torch.distributions as dist
input_data = torch.randn(3, 4)
reshape_transform = dist.transforms.ReshapeTransform((3, 4), (4, 3))
print(reshape_transform(input_data))