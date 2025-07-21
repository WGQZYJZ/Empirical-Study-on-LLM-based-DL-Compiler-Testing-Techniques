'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 4
hidden_size = 3
num_layers = 2
input_data = torch.randn(10, 3, 4)
lstm = nn.LSTM(input_size, hidden_size, num_layers)
(output, (h, c)) = lstm(input_data)
print(output)
print(h)
print(c)