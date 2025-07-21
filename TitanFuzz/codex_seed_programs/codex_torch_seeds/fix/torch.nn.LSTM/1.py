'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
input_size = 3
hidden_size = 3
num_layers = 1
batch_size = 1
seq_len = 2
data = Variable(torch.randn(seq_len, batch_size, input_size))
lstm = nn.LSTM(input_size, hidden_size, num_layers)
(output, (h_n, c_n)) = lstm(data)
print(output)
print(h_n)
print(c_n)