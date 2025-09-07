import torch
from torch import nn
from torch.autograd import Variable

x = torch.randn(5, 3, 2, 2)
y = torch.nn.functional.dropout3d(x, p=0.5, training=True, inplace=False)