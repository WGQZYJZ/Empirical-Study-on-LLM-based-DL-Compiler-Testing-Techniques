'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ReshapeTransform\ntorch.distributions.transforms.ReshapeTransform(in_shape, out_shape, cache_size=0)\n'
import torch
input_data = torch.rand(size=(2, 3))
trans = torch.distributions.transforms.ReshapeTransform(in_shape=(2, 3), out_shape=(3, 2))
output = trans(input_data)
print('input_data:', input_data)
print('output:', output)