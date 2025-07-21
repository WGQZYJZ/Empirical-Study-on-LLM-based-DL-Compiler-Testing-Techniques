import torch
from torch import nn
from torch.autograd import Variable
row = 3
col = 3
indices = torch.tril_indices(row=row, col=col)