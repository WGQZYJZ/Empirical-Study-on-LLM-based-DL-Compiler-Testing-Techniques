'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import numpy as np
import torch
input_size = 3
hidden_size = 4
input = torch.randn(4, 3, requires_grad=True)
hx = torch.randn(4, 4, requires_grad=True)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
print(gru_cell(input, hx))
print(gru_cell(input, hx).size())