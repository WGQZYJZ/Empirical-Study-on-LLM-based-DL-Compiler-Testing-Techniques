'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 10
hidden_size = 20
input = torch.randn(3, input_size)
hx = torch.randn(3, hidden_size)
gru_cell = nn.GRUCell(input_size, hidden_size)
output = gru_cell(input, hx)
print('output: ', output)