'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
x = torch.randn(1, 1)
transform = torch.distributions.transforms.ExpTransform(cache_size=0)
print(transform(x))