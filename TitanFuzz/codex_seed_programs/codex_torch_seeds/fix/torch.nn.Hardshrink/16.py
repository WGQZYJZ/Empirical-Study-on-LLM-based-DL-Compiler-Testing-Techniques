'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
input_data = torch.randn(3, 5)
print('Input data: ', input_data)
torch.nn.Hardshrink(lambd=0.5)
torch.nn.Hardshrink(lambd=0.5)(input_data)