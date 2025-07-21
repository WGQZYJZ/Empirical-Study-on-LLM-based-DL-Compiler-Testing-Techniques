import torch
from torch import nn
from torch.autograd import Variable
a = torch.arange(1, 10, dtype=torch.float)
b = torch.square(a)