import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16)
output = torch.nn.AlphaDropout(p=0.5, inplace=False)(input)
input = torch.randn(20, 16)
output = torch.nn.Dropout(p=0.5, inplace=False)(input)