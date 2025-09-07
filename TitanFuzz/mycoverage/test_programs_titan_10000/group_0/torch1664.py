import torch
from torch import nn
from torch.autograd import Variable

row = 2
col = 4
output = torch.triu_indices(row, col)