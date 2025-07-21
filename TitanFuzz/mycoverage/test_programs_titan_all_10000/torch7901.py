import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([(- float('inf')), (- 1), 0, 1, float('inf'), float('nan')])
torch.isneginf(input)