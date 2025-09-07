import torch
from torch import nn
from torch.autograd import Variable
input_size = 3
hidden_size = 2
x = torch.randn(1, input_size)
h = torch.randn(1, hidden_size)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
h_next = gru_cell(x, h)