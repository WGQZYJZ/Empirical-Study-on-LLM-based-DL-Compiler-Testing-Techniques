'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
input_size = 3
hidden_size = 2
x = torch.randn(1, input_size)
h = torch.randn(1, hidden_size)
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
h_next = gru_cell(x, h)
print('h_next: ', h_next)