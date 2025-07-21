import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor([float('inf'), float('-inf'), float('nan'), float('nan')])
y = torch.isinf(x)