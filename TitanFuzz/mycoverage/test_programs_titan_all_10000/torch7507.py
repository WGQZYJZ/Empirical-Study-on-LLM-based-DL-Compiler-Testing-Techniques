import torch
from torch import nn
from torch.autograd import Variable
row = 3
col = 4
torch.tril_indices(row, col, offset=0, dtype=torch.long, device='cpu', layout=torch.strided)