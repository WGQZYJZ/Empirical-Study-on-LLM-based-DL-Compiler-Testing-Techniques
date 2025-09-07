import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(3, 4)
abs_transform = torch.distributions.transforms.AbsTransform()
abs_transform(x)