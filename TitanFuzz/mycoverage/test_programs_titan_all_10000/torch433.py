import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(5, 5)
dropout = torch.nn.Dropout(p=0.5, inplace=False)
y = dropout(x)