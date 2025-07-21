'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
print(input_data)
tanh_layer = torch.nn.Tanh()
output = tanh_layer(input_data)
print(output)