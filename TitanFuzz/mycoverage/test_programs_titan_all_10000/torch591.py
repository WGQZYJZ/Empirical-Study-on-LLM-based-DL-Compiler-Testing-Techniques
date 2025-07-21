import torch
from torch import nn
from torch.autograd import Variable
x = torch.arange((- 10), 10, 0.1)
y = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(x)