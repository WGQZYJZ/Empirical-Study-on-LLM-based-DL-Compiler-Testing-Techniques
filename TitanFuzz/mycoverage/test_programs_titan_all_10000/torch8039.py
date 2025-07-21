import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 5)
m = torch.nn.AlphaDropout(p=0.5, inplace=False)
m = torch.nn.AlphaDropout(p=0.5, inplace=True)
output = m(input)