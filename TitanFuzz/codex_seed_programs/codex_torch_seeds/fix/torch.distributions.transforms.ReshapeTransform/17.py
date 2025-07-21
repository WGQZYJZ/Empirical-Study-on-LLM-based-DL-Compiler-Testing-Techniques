'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
data = torch.randn(4, 2, 3)
print(data)
reshape = torch.distributions.transforms.ReshapeTransform(in_shape=(4, 2, 3), out_shape=(3, 8))
print(reshape(data))