import torch
from torch import nn
from torch.autograd import Variable

x = torch.rand(5, 5)
abs_transform = torch.distributions.transforms.AbsTransform()