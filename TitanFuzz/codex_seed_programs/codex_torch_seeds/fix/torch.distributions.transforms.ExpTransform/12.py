'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
import torch
data = torch.randn(2, 3)
print(data)
transform = transforms.ExpTransform(cache_size=0)
print(transform(data))