import torch
from torch import nn
from torch.autograd import Variable
row = 3
col = 4
result = torch.tril_indices(row, col)