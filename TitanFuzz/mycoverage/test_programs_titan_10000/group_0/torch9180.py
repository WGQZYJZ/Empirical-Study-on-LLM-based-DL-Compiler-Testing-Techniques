import torch
from torch import nn
from torch.autograd import Variable

x = torch.arange(0, 10, 0.1)
y = torch.arange(0, 10, 0.1, out=torch.FloatTensor())