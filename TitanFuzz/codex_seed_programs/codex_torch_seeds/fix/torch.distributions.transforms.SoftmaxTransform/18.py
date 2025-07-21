'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.distributions.transforms.SoftmaxTransform\ntorch.distributions.transforms.SoftmaxTransform(cache_size=0)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torchvision import datasets, transforms
from torch.autograd import Variable
from torch.distributions import constraints
from torch.distributions.transforms import Transform, SigmoidTransform, AffineTransform, SoftmaxTransform, PowerTransform
import torch
x = torch.randn(2, 3)
print(x)
torch.distributions.transforms.SoftmaxTransform(cache_size=0)