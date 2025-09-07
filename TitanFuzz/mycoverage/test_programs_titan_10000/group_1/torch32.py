import torch
from torch import nn
from torch.autograd import Variable

a = torch.arange(9, dtype=torch.float)
b = torch.float_power(a, 2)