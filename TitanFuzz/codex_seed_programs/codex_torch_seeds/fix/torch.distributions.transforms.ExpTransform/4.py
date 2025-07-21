'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
input_data = torch.rand(100)
exp_transform = ExpTransform(cache_size=0)
output = exp_transform(input_data)
print('output:', output)