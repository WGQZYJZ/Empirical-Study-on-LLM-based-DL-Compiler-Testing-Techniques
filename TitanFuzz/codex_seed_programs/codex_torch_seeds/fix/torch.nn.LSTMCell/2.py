'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
from torch.autograd import Variable
input_size = 5
hidden_size = 3
batch_size = 1
num_layers = 1
input = Variable(torch.randn(batch_size, input_size))
h_0 = Variable(torch.randn(batch_size, hidden_size))
c_0 = Variable(torch.randn(batch_size, hidden_size))
lstm = nn.LSTMCell(input_size, hidden_size)
output = []
for i in range(6):
    (h_0, c_0) = lstm(input, (h_0, c_0))
    output.append(h_0)
for j in range(6):
    print(output[j])