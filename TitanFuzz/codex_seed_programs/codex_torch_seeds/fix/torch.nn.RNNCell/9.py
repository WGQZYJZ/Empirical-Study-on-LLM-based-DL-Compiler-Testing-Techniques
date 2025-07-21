"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
input_size = 5
hidden_size = 3
input = torch.randn(10, 3, input_size)
rnn = nn.RNNCell(input_size, hidden_size)
output = []
hx = torch.randn(3, hidden_size)
for i in range(10):
    hx = rnn(input[i], hx)
    output.append(hx)
print(output)