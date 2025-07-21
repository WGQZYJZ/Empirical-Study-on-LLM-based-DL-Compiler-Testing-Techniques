'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
data = torch.randn(4, 3, 2)
reshape_transform = transforms.ReshapeTransform((4, 3, 2), (4, 6))
print(reshape_transform(data))
reshape_transform = transforms.ReshapeTransform((2, 3, 4), (3, 8))
print(reshape_transform(data))