'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
input_size = 2
hidden_size = 3
num_layers = 1
seq_len = 3
batch_size = 3
input_data = torch.randn(seq_len, batch_size, input_size)
print('input_data: ', input_data)
gru = nn.GRU(input_size, hidden_size, num_layers)
h0 = torch.randn(num_layers, batch_size, hidden_size)
(output, hn) = gru(input_data, h0)
print('output: ', output)
print('hn: ', hn)