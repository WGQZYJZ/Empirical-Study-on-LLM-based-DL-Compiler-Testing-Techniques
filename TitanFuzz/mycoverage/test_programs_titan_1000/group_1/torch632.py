import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange(1, 11, dtype=torch.float)
y = torch.log10(x)