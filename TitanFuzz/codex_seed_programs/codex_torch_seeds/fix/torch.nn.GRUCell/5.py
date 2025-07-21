'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
from torch import nn
input_size = 3
hidden_size = 2
batch_size = 1
input = torch.randn(batch_size, input_size)
h_0 = torch.randn(batch_size, hidden_size)
gru_cell = nn.GRUCell(input_size, hidden_size)
h_1 = gru_cell(input, h_0)
print(h_1)