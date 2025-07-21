'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 5
hidden_size = 3
batch_size = 2
seq_len = 3
input_data = torch.randn(seq_len, batch_size, input_size)
h0 = torch.randn(batch_size, hidden_size)
gru_cell = nn.GRUCell(input_size, hidden_size)
h = h0
for i in range(seq_len):
    h = gru_cell(input_data[i], h)
print(h)