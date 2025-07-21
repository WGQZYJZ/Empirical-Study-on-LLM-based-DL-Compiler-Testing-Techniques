'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
from torch import nn
x = torch.randn(3, 3)
h = torch.randn(3, 3)
c = torch.randn(3, 3)
lstm_cell = nn.LSTMCell(3, 3)
hx = (h, c)
hx = lstm_cell(x, hx)
print(hx)