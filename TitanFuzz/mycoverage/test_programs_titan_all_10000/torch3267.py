import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange((- 10), 10, 0.1)
y = torch.special.ndtr(x)