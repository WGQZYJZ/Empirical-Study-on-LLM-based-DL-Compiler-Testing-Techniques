'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
from torch import nn
import torch
import numpy as np
input_size = 10
hidden_size = 20
batch_size = 32
input_data = torch.randn(batch_size, input_size)
hx = torch.randn(batch_size, hidden_size)
cx = torch.randn(batch_size, hidden_size)
lstm_cell = nn.LSTMCell(input_size, hidden_size)
(hx, cx) = lstm_cell(input_data, (hx, cx))
print(hx.shape)
print(cx.shape)