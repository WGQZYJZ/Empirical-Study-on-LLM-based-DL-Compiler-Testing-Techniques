'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import numpy as np
input_data = np.random.randn(2, 3)
gru = torch.nn.GRUCell(3, 2)
output = gru(torch.tensor(input_data, dtype=torch.float32))
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import numpy as np
input_data = np.random.randn(2, 3)