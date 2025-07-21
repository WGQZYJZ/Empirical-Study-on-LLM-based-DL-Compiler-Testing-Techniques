'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import numpy as np
input_size = 2
hidden_size = 3
num_layers = 1
lstm = torch.nn.LSTM(input_size, hidden_size, num_layers)
input = torch.randn(1, 1, input_size)
h0 = torch.randn(num_layers, 1, hidden_size)
c0 = torch.randn(num_layers, 1, hidden_size)
(out, (hn, cn)) = lstm(input, (h0, c0))
print(out)
print(hn)
print(cn)