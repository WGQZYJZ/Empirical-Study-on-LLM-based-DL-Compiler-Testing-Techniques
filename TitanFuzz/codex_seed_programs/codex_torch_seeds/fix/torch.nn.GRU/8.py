'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_size = 4
hidden_size = 2
gru = nn.GRU(input_size, hidden_size)
input = torch.randn(3, 2, 4)
h0 = torch.randn(1, 2, 2)
(output, hn) = gru(input, h0)
print('output size: ', output.size())
print('hn size: ', hn.size())
gru = nn.GRU(input_size, hidden_size, num_layers=2)
h0 = torch.randn(2, 2, 2)
(output, hn) = gru(input, h0)