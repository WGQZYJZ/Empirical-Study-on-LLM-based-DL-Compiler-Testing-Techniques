'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.TanhTransform\ntorch.distributions.transforms.TanhTransform(cache_size=0)\n'
import torch
x = torch.randn(3, 5)
tanh_trans = torch.distributions.transforms.TanhTransform(cache_size=0)
y = tanh_trans(x)
print('Input data: ', x)
print('Output data: ', y)