import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 16)
dropout = torch.nn.AlphaDropout(p=0.5, inplace=False)
output = dropout(input)