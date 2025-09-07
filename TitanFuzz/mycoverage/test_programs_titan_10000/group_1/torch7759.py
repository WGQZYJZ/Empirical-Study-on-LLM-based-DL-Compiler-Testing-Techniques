import torch
from torch import nn
from torch.autograd import Variable

x = torch.tensor([1, 2, float('inf'), float('nan')])
y = torch.isfinite(x)