import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(100, 100)
dropout = torch.nn.Dropout(p=0.5, inplace=False)
y = dropout(x)