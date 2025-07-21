'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SoftmaxTransform\ntorch.distributions.transforms.SoftmaxTransform(cache_size=0)\n'
import torch
import torch.distributions.transforms as tdt
x = torch.randn(3, 3)
print(x)
y = tdt.SoftmaxTransform().inv(x)
print(y)