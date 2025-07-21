'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
input_size = 4
hidden_size = 2
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
input = torch.randn(6, 3, input_size)
hx = torch.randn(3, hidden_size)
output = []
for i in input:
    hx = gru_cell(i, hx)
    output.append(hx)
print(output)