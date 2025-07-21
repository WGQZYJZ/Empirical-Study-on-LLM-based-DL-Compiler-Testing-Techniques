import torch
from torch import nn
from torch.autograd import Variable
row = 5
col = 5
torch.triu_indices(row, col)
torch.triu_indices(row, col, offset=1)
torch.triu_indices(row, col, offset=2)
torch.triu_indices(row, col, offset=3)
torch.triu_indices(row, col, offset=4)
torch.triu_indices(row, col, offset=5)