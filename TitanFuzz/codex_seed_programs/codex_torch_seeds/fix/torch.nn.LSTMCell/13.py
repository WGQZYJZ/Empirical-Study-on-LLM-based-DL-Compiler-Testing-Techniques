'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
from torch import nn
import torch
from torch import nn
input = torch.randn(3, 3)
hx = torch.randn(3, 3)
cx = torch.randn(3, 3)
lstm = nn.LSTMCell(3, 3)
(hx, cx) = lstm(input, (hx, cx))
print(hx)
print(cx)