import torch
from torch import nn
from torch.autograd import Variable
row = 5
col = 5
indices = torch.triu_indices(row, col, offset=0, dtype=torch.long)