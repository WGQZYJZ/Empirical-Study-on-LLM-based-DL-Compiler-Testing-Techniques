'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SoftmaxTransform\ntorch.distributions.transforms.SoftmaxTransform(cache_size=0)\n'
import torch
from torch import nn
from torch.distributions import transforms
import torch
from torch import nn
from torch.distributions import transforms
x = torch.rand(10, 3)
print(x)
softmax = transforms.SoftmaxTransform(cache_size=0)
print(softmax(x))