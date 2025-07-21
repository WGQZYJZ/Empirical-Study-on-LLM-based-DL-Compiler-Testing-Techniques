import torch
from torch import nn
from torch.autograd import Variable
data = torch.arange(1, 11)
output = torch.repeat_interleave(data, repeats=2, dim=0)