import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3)
row = 3
col = 3
offset = 0
tril_indices = torch.tril_indices(row, col, offset)
tril_data = torch.tril(input_data)