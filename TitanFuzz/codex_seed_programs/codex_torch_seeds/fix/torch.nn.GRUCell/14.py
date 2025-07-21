'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
from torch.nn import GRUCell
input_size = 5
hidden_size = 3
input = torch.randn(6, 3, 5)
hx = torch.randn(3, 3)
grucell = GRUCell(input_size, hidden_size)
output = []
for i in input:
    hx = grucell(i, hx)
    output.append(hx)
print(output)