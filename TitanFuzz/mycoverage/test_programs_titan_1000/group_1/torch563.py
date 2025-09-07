import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16, 50, 32)
torch.nn.FractionalMaxPool2d(3, output_size=13, _random_samples=None)