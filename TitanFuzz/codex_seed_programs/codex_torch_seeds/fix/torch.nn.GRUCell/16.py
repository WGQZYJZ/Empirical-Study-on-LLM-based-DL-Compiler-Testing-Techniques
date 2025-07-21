'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch
input = torch.randn(3, 4)
hx = torch.randn(3, 4)
gru_cell = torch.nn.GRUCell(4, 4)
output = gru_cell(input, hx)
print(output)