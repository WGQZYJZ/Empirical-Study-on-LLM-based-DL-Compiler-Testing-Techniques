import torch
from torch import nn
from torch.autograd import Variable

input = torch.randn(10, 10)
dropout = torch.nn.Dropout(p=0.5, inplace=False)
output = dropout(input)