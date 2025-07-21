'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
input_size = 10
hidden_size = 20
lstm_cell = torch.nn.LSTMCell(input_size, hidden_size)
print(lstm_cell)