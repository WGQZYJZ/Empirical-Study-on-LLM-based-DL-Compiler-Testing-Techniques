'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import numpy as np
batch_size = 1
input_size = 4
hidden_size = 2
input_data = torch.randn(batch_size, input_size)
print(input_data)
gru_cell = nn.GRUCell(input_size, hidden_size)
output = gru_cell(input_data)
print(output)