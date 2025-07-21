'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
from torch import nn
import numpy as np
input = torch.randn(5, 3, 10)
h0 = torch.randn(1, 3, 20)
c0 = torch.randn(1, 3, 20)
rnn = nn.GRU(10, 20, 1)
(output, hn) = rnn(input, h0)
print(output.size())
print(hn.size())
lstm = nn.LSTM(10, 20, 1)