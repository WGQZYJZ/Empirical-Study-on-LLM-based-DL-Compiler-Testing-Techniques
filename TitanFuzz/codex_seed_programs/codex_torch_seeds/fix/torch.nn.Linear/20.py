'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Linear\ntorch.nn.Linear(in_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
input_data = torch.randn(1, 10)
print('input_data:', input_data)
linear_layer = torch.nn.Linear(10, 1)
print('linear_layer:', linear_layer)
output = linear_layer(input_data)
print('output:', output)