'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTM\ntorch.nn.LSTM(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, proj_size=0, device=None, dtype=None)\n'
import torch
seq_len = 3
batch_size = 2
input_size = 4
hidden_size = 3
num_layers = 1
input = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn(num_layers, batch_size, hidden_size)
c0 = torch.randn(num_layers, batch_size, hidden_size)
rnn = torch.nn.LSTM(input_size, hidden_size, num_layers)
(output, (hn, cn)) = rnn(input, (h0, c0))
print(output)
print(hn)
print(cn)