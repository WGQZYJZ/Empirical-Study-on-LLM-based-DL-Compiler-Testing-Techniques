'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRU\ntorch.nn.GRU(input_size, hidden_size, num_layers=1, bias=True, batch_first=False, dropout=0.0, bidirectional=False, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
lstm_input_size = 2
lstm_hidden_size = 4
lstm_num_layers = 1
lstm = nn.GRU(lstm_input_size, lstm_hidden_size, lstm_num_layers)
print('lstm: ', lstm)
input_data = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
input_data = torch.tensor(input_data, dtype=torch.float)
print('input_data: ', input_data)
hidden_state = torch.zeros(lstm_num_layers, lstm_hidden_size)