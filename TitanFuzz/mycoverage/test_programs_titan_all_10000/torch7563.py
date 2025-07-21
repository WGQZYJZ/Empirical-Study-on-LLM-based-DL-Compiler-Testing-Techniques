import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([1, float('nan'), float('inf')])
y = torch.isnan(x)