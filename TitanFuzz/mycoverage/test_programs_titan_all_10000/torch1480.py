import torch
from torch import nn
from torch.autograd import Variable
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)