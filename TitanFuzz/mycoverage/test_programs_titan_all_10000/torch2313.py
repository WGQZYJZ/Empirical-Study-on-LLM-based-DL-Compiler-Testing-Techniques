import torch
from torch import nn
from torch.autograd import Variable
in_data = torch.arange(1, 10, dtype=torch.float)
out = torch.special.digamma(in_data)