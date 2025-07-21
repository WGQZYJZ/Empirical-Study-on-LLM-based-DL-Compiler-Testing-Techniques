'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import numpy as np
import torch
import numpy as np
input_size = 5
hidden_size = 3
seq_len = 3
batch_size = 2
input = torch.randn(seq_len, batch_size, input_size)
hx = torch.randn(batch_size, hidden_size)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
hx = gru_cell(input[0], hx)
print(hx)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
hx = gru_cell(input[0], hx)
print(hx)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
hx