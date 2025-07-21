'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.TanhTransform\ntorch.distributions.transforms.TanhTransform(cache_size=0)\n'
import torch
from torch.distributions.transforms import TanhTransform
x = torch.tensor([(- 1), 0, 1])
tanh_transform = TanhTransform(cache_size=0)
y = tanh_transform(x)
print(y)