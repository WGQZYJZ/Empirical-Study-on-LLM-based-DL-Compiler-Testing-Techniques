'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(5, 3, 10)
h_0 = torch.randn(2, 3, 20)
rnn = nn.GRU(10, 20, 2)
(output, h_n) = rnn(input, h_0)
print(output.size(), h_n.size())