'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 4
hidden_size = 2
batch_size = 1
input = torch.Tensor(1, 1, input_size)
h_0 = torch.Tensor(1, batch_size, hidden_size)
rnn = nn.GRU(input_size, hidden_size, batch_first=True)
(output, h_n) = rnn(input, h_0)
print(output)
print(h_n)