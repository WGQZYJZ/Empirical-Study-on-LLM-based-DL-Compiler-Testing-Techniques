import torch
from torch import nn
from torch.autograd import Variable
input_size = 5
hidden_size = 3
input = torch.randn(6, 3, 5)
hx = torch.randn(3, 3)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
output = []
for i in range(6):
    h_in = input[i, :, :]
    h_out = gru_cell(h_in, hx)
    output.append(h_out)
    hx = h_out