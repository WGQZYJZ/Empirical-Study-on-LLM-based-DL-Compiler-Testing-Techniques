import torch
from torch import nn
from torch.autograd import Variable
x = torch.ones(1, 1, 2, 2)
torch.nn.Dropout2d(p=0.5, inplace=False)(x)