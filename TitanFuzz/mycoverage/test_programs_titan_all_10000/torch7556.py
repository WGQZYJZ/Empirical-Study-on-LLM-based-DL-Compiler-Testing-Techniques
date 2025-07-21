import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(100, 200)
dropout = torch.nn.Dropout(p=0.5)
y = dropout(x)