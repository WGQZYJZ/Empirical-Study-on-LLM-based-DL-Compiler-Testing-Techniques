import torch
from torch import nn
from torch.autograd import Variable
row = 5
col = 10
offset = 2
torch.tril_indices(row, col, offset)
row = 5
col = 10
offset = 2
torch.triu_indices(row, col, offset)