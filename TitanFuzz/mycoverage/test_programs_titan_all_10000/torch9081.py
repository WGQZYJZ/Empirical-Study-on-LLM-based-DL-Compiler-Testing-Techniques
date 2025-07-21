import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3)
y = torch.nn.AlphaDropout(p=0.5, inplace=False)(x)