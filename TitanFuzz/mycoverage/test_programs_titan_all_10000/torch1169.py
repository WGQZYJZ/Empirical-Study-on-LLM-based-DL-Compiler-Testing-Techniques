import torch
from torch import nn
from torch.autograd import Variable
input = torch.tensor([float('-inf'), float('inf'), float('nan'), float('-inf'), float('inf'), float('nan'), float('-inf'), float('inf'), float('nan')])
output = torch.isneginf(input)