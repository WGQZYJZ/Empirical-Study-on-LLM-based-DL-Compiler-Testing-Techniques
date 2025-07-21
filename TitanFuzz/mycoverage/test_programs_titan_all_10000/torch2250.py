import torch
from torch import nn
from torch.autograd import Variable
input_size = 5
hidden_size = 3
seq_len = 3
batch_size = 2
input = torch.randn(seq_len, batch_size, input_size)
hx = torch.randn(batch_size, hidden_size)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
hx = gru_cell(input[0], hx)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
hx = gru_cell(input[0], hx)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
hx