'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(3, 3)
cell = nn.LSTMCell(3, 5)
'\nTask 1: Generate input and hidden data\nTask 2: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.randn(3, 3)
hidden_data = torch.randn(3, 5)
cell = nn.LSTMCell(3, 5)