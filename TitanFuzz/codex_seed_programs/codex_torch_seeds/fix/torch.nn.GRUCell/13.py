'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch
input_size = 3
hidden_size = 5
gru_cell = torch.nn.GRUCell(input_size, hidden_size)
print('Parameters of the GRU cell:')
for param in gru_cell.parameters():
    print(param)
print('\nOutput of the GRU cell:')
input = torch.randn(4, 3)
hx = torch.randn(4, 5)
output = gru_cell(input, hx)
print(output)