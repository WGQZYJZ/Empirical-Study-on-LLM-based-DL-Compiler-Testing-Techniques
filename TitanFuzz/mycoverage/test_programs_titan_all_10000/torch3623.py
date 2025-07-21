import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 3)
sigmoid_transform = torch.distributions.transforms.SigmoidTransform(cache_size=0)