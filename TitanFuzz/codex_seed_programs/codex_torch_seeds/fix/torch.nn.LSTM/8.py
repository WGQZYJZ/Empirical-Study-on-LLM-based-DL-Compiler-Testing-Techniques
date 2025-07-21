'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 2
hidden_size = 3
num_layers = 1
input_data = torch.Tensor([[[1, 2], [2, 2], [3, 4], [4, 5]], [[1, 2], [2, 2], [3, 4], [4, 5]]])
lstm = nn.LSTM(input_size, hidden_size, num_layers)
(output, (h_n, c_n)) = lstm(input_data)
print('Output ', output)
print('h_n ', h_n)
print('c_n ', c_n)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'