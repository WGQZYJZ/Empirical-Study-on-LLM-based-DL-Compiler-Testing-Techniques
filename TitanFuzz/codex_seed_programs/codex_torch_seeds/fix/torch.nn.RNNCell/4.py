"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
input_data = torch.randn(5, 3, 10)
rnn = nn.RNNCell(10, 20)
hx = torch.randn(3, 20)
output = []
for i in range(5):
    hx = rnn(input_data[i], hx)
    output.append(hx)
print(output)