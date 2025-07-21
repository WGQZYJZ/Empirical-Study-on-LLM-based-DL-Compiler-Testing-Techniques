'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_size = 4
hidden_size = 2
num_layers = 1
batch_size = 1
seq_len = 6
input = torch.randn(seq_len, batch_size, input_size)
print('Input data: ', input)
gru = nn.GRU(input_size, hidden_size, num_layers)
hidden = torch.randn(num_layers, batch_size, hidden_size)
print('Initial hidden state: ', hidden)
(out, hidden) = gru(input, hidden)
print('Output: ', out)
print('Hidden: ', hidden)