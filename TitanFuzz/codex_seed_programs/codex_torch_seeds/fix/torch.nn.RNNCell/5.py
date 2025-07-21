"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
input_size = 10
hidden_size = 5
x = torch.randn(3, 1, input_size)
print(x)
rnn = nn.RNNCell(input_size, hidden_size)
h = torch.randn(1, hidden_size)
print(h)
for i in range(3):
    h = rnn(x[i], h)
    print(h)