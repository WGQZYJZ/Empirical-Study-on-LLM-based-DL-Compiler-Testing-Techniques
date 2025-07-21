'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 3
hidden_size = 4
batch_size = 2
input = torch.randn(batch_size, input_size)
hx = torch.randn(batch_size, hidden_size)
cx = torch.randn(batch_size, hidden_size)
lstm = nn.LSTMCell(input_size, hidden_size)
(hx, cx) = lstm(input, (hx, cx))
print(hx, cx)