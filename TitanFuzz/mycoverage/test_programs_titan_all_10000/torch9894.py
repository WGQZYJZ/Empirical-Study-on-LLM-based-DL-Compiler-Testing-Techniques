import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(4, 4)
softmax_transform = torch.distributions.transforms.SoftmaxTransform(cache_size=0)
y = softmax_transform(x)