'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 4
hidden_size = 2
rnn = nn.GRU(input_size, hidden_size)
input = torch.randn(5, 3, input_size)
h0 = torch.randn(1, 3, hidden_size)
(output, hn) = rnn(input, h0)
print('input:', input.shape)
print('h0:', h0.shape)
print('output:', output.shape)
print('hn:', hn.shape)