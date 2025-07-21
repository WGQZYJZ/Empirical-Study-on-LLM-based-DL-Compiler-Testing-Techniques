'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_size = 5
hidden_size = 3
batch_size = 1
seq_len = 3
input = torch.randn(seq_len, batch_size, input_size)
rnn = nn.GRU(input_size, hidden_size)
(output, h_n) = rnn(input)
print(output)
print(h_n)
'\nTask 5: Get the output of all time steps\nTask 6: Get the output of the last time step\nTask 7: Get the output of the first time step\n'
(output, h_n) = rnn(input)
print(output)
print(output[(- 1)])