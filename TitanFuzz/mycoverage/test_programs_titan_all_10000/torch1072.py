import torch
from torch import nn
from torch.autograd import Variable
input_size = 2
hidden_size = 3
num_layers = 1
lstm = torch.nn.LSTM(input_size, hidden_size, num_layers)
input = torch.randn(1, 1, input_size)
h0 = torch.randn(num_layers, 1, hidden_size)
c0 = torch.randn(num_layers, 1, hidden_size)
(out, (hn, cn)) = lstm(input, (h0, c0))