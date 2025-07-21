'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([[[1, 2, 3], [4, 5, 6]]], dtype=torch.float32)
gru = nn.GRU(input_size=3, hidden_size=2, batch_first=True)
(output, h_n) = gru(input_data)
print(output)
print(h_n)