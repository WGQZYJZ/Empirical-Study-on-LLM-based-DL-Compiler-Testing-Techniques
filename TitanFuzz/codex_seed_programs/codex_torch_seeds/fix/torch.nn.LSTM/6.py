'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import torch
input_size = 5
batch = 4
seq_len = 3
input = torch.randn(seq_len, batch, input_size)
lstm = nn.LSTM(input_size, 3)
(output, (hn, cn)) = lstm(input)
print(output)
print(hn)