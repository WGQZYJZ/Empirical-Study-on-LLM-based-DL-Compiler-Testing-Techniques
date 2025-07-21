'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(3, 5)
h = torch.randn(3, 5)
rnn = nn.GRUCell(5, 5)
h_next = rnn(x, h)
print(h_next)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(3, 5, 5)
h = torch.randn(1, 3, 5)
rnn = nn.GRU(5, 5, 1)