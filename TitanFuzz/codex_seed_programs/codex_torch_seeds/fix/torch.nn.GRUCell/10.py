'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.GRUCell\ntorch.nn.GRUCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F
x = torch.randn(3, 5)
h = torch.randn(3, 5)
gru_cell = nn.GRUCell(5, 5)
h_new = gru_cell(x, h)
print(h_new)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.LSTMCell\ntorch.nn.LSTMCell(input_size, hidden_size, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
import torch.nn as nn
import torch.nn.functional as F