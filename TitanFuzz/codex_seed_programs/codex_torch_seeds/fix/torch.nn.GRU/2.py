'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
batch_size = 1
input_size = 3
hidden_size = 3
num_layers = 1
seq_len = 3
input = torch.randn(seq_len, batch_size, input_size)
gru = nn.GRU(input_size, hidden_size, num_layers)
gru_bi = nn.GRU(input_size, hidden_size, num_layers, bidirectional=True)
gru_dropout = nn.GRU(input_size, hidden_size, num_layers, dropout=0.5)