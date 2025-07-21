'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 4
hidden_size = 3
batch_size = 2
seq_len = 3
input = torch.randn(seq_len, batch_size, input_size)
hx = torch.randn(batch_size, hidden_size)
cx = torch.randn(batch_size, hidden_size)
lstm_cell = nn.LSTMCell(input_size, hidden_size)
output = []
for i in range(seq_len):
    (hx, cx) = lstm_cell(input[i], (hx, cx))
    output.append(hx)
print('output:', output)