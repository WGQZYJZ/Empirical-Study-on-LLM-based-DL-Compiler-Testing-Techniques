'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 5
hidden_size = 3
num_layers = 1
input_data = torch.randn(1, 1, input_size)
print(input_data)
gru = nn.GRU(input_size, hidden_size, num_layers)
print(gru)
(output, h_n) = gru(input_data)
print(output)
print(h_n)