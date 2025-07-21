'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
x = torch.randn(3, 5)
h = torch.randn(3, 5)
rnn = torch.nn.GRUCell(5, 5)
output = rnn(x, h)
print(output)