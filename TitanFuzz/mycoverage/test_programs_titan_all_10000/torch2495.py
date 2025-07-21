import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(1, 1, 3, 3)
y = torch.nn.functional.dropout(x, p=0.5, training=True, inplace=False)