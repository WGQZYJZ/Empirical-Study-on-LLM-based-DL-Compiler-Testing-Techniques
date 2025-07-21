import torch
from torch import nn
from torch.autograd import Variable
in_data = torch.randn(6, 3)
out_data = torch.special.i0(in_data)