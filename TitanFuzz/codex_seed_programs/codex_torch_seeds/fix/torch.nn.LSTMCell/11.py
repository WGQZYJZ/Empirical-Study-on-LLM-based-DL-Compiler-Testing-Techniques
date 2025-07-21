'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import numpy as np
import torch
input_size = 5
hidden_size = 10
batch_size = 2
seq_len = 3
input = torch.randn(seq_len, batch_size, input_size)
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)
hx = torch.randn(batch_size, hidden_size)
cx = torch.randn(batch_size, hidden_size)
output = []
for i in range(seq_len):
    (hx, cx) = lstm_cell(input[i], (hx, cx))
    output.append(hx)
print(output[(- 1)])