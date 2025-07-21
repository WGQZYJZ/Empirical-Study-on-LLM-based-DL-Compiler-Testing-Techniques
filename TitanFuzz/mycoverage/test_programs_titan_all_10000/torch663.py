import torch
from torch import nn
from torch.autograd import Variable
x = torch.randn(2, 3, 4, 4, 4)
torch.nn.Dropout3d(p=0.5, inplace=False)(x)
x = torch.randn(2, 3, 4, 4)
torch.nn.Dropout2d(p=0.5, inplace=False)(x)