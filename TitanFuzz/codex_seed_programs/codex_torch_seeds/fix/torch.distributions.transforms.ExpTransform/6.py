'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
data = torch.rand(4, requires_grad=True)
print(data)
transformed_data = ExpTransform().inv(data)
print(transformed_data)