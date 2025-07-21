'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
data = torch.rand(10, 10)
exp_transform = ExpTransform()
transformed_data = exp_transform(data)
print('The original data:', data)
print('The transformed data:', transformed_data)