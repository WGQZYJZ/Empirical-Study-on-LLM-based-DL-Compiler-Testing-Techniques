'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
batch_size = 3
input_size = 2
hidden_size = 4
gru_cell = nn.GRUCell(input_size, hidden_size)
x = torch.randn(batch_size, input_size)
h = torch.randn(batch_size, hidden_size)
output = gru_cell(x, h)
print(output)