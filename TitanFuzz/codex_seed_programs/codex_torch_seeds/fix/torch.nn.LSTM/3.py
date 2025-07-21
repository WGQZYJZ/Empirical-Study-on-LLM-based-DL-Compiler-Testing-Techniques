'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(3, 5, 7)
print(x)
lstm = nn.LSTM(7, 5)
(out, (h, c)) = lstm(x)
print(out)
print(h)
print(c)
(out, (h, c)) = lstm(x, (h, c))
print(out)
print(h)
print(c)
(out, (h, c)) = lstm(x, (h, c))
print(out)
print(h)
print(c)