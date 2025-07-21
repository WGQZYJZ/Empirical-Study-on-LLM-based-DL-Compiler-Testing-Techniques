"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
rnn = nn.RNNCell(3, 2)
print(rnn)
rnn_bias = nn.RNNCell(3, 2, bias=True)
print(rnn_bias)
rnn_nonlinearity = nn.RNNCell(3, 2, nonlinearity='relu')
print(rnn_nonlinearity)
rnn_device = nn.RNNCell(3, 2, device='cuda')
print(rnn_device)