'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import ExpTransform
x = torch.randn(10)
print(x)
exp_transform = ExpTransform()
print(exp_transform(x))