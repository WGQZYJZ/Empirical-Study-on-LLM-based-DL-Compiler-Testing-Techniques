import torch
from torch import nn
from torch.autograd import Variable
row = torch.tensor(3)
col = torch.tensor(3)
tril_indices = torch.tril_indices(row, col)