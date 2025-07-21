'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
x = torch.randn(1000)
transform = transforms.ExpTransform(cache_size=0)
y = transform(x)
print(y)