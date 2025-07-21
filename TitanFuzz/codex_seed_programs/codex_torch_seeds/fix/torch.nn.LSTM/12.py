'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(5, 3, 7)
lstm = nn.LSTM(7, 3)
(out, hn) = lstm(input_data)
print(out.size(), hn[0].size(), hn[1].size())