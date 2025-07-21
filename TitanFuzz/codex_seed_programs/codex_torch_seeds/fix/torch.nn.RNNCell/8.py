"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
input = torch.randn(6, 3, 10)
rnn = nn.RNNCell(10, 20)
hx = torch.randn(3, 20)
output = []
for i in range(6):
    hx = rnn(input[i], hx)
    output.append(hx)
print(output)