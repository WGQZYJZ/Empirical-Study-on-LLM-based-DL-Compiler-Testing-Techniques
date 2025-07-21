'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch
input_data = torch.randn(1, 1, 3)
linear_layer = nn.Linear(3, 1)
relu_layer = F.relu(linear_layer(input_data))
print(relu_layer)