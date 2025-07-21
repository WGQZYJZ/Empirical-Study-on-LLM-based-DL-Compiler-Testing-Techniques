'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as transforms
X = torch.rand(3, 3)
exp_transform = transforms.ExpTransform(cache_size=0)
print(exp_transform(X))