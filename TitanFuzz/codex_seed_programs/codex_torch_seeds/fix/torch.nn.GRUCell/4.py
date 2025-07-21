'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_size = 3
hidden_size = 4
batch_size = 2
device = torch.device('cpu')
gru_cell = nn.GRUCell(input_size, hidden_size, bias=True, device=device)
print(gru_cell)