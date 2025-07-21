"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.utils.remove_weight_norm\ntorch.nn.utils.remove_weight_norm(module, name='weight')\n"
import torch
from torch import nn
input_size = 10
hidden_size = 10
input = torch.randn(2, 3, 4)
linear = nn.Linear(input_size, hidden_size)
weight_norm = nn.utils.weight_norm(linear, name='weight')
removed_weight_norm = nn.utils.remove_weight_norm(weight_norm)
print(removed_weight_norm)