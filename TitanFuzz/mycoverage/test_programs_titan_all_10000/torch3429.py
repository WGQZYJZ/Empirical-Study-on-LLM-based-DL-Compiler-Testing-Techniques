import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(3, 4)
hx = torch.randn(3, 4)
gru_cell = torch.nn.GRUCell(4, 4)
output = gru_cell(input, hx)