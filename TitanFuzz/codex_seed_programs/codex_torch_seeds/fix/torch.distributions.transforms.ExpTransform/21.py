'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.ExpTransform\ntorch.distributions.transforms.ExpTransform(cache_size=0)\n'
import torch
import torch.distributions.constraints as constraints
import torch.distributions.transforms as transforms
import torch
import torch.distributions.constraints as constraints
import torch.distributions.transforms as transforms
x = torch.randn(3)
trans = transforms.ExpTransform(cache_size=0)
print(trans(x))