"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RNNCell\ntorch.nn.RNNCell(input_size, hidden_size, bias=True, nonlinearity='tanh', device=None, dtype=None)\n"
import torch
import torch.nn as nn
input_size = 5
hidden_size = 10
batch_size = 1
input_data = torch.randn(batch_size, input_size)
rnn = nn.RNNCell(input_size, hidden_size)
print(rnn)
hidden = torch.randn(batch_size, hidden_size)
output = rnn(input_data, hidden)
print(output)
'\nTask 4: Call the API torch.nn.RNN\ntorch.nn.RNN(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 5
hidden_size = 10
batch_size = 1
num_layers = 1
input_data = torch.randn(batch_size, input_size)