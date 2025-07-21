'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_size = 3
hidden_size = 4
batch_size = 1
input = torch.randn(batch_size, input_size)
hx = torch.randn(batch_size, hidden_size)
gru_cell = nn.GRUCell(input_size, hidden_size)
hx = gru_cell(input, hx)
print(hx)
gru = nn.GRU(input_size, hidden_size)
(output, hx) = gru(input.unsqueeze(0), hx.unsqueeze(0))
print(output)
print(hx)