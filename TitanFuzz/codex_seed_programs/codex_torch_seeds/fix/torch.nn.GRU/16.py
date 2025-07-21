'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 4
hidden_size = 2
num_layers = 1
num_directions = 1
batch_size = 1
seq_len = 6
input_data = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn((num_layers * num_directions), batch_size, hidden_size)
c0 = torch.randn((num_layers * num_directions), batch_size, hidden_size)
print('input_data: ', input_data)
print('h0: ', h0)
print('c0: ', c0)
rnn = nn.GRU(input_size, hidden_size, num_layers, batch_first=False)
(output, hn) = rnn(input_data, h0)
print('output: ', output)