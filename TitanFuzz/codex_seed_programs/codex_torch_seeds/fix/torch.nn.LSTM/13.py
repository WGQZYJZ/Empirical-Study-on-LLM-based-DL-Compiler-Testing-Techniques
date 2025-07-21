'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input = torch.randn(5, 3, 10)
print(input.shape)
rnn = nn.LSTM(10, 20, 2)
(output, (hn, cn)) = rnn(input)
print(output.shape)
print(hn.shape)
print(cn.shape)
rnn = nn.LSTM(10, 20, 2, bidirectional=True)
(output, (hn, cn)) = rnn(input)
print(output.shape)
print(hn.shape)
print(cn.shape)
rnn = nn.LSTM(10, 20, 2, bidirectional=True, batch_first=True)