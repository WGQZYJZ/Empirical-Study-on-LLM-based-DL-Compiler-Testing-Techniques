"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
batch_size = 1
input_size = 3
hidden_size = 3
seq_len = 5
input_data = torch.randn(batch_size, input_size)
rnn = nn.RNNCell(input_size, hidden_size)
hidden = torch.randn(batch_size, hidden_size)
for i in range(seq_len):
    hidden = rnn(input_data, hidden)
    print(hidden)