'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
x = torch.randn(3, 1, 4)
rnn = nn.GRU(4, 3, 1)
(out, h) = rnn(x, torch.zeros(1, 1, 3))
print(out)
print(h)