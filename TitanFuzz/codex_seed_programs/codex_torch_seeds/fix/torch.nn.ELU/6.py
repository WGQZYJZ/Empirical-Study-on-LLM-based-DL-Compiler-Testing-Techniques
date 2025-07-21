'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 1), 0, 1, 2], dtype=torch.float)
elu_layer = nn.ELU()
output = elu_layer(input_data)
print('input:', input_data)
print('output:', output)
'\nTask 4: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
import torch.nn as nn
input_data = torch.tensor([(- 1), 0, 1, 2], dtype=torch.float)
hardshrink_layer = nn.Hardshrink()
output = hardshrink_layer(input_data)
print('input:', input_data)
print('output:', output)