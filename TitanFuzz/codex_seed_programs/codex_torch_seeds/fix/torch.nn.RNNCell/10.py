"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
X = torch.randn(3, 1, 2)
print('Task 3: Call the API torch.nn.RNNCell')
rnn = nn.RNNCell(input_size=2, hidden_size=3)
h = torch.randn(1, 3)
output = []
for i in range(X.size(0)):
    h = rnn(X[i], h)
    output.append(h)
print(output)