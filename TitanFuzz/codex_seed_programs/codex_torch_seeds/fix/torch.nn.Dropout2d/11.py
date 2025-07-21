'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
input_data = torch.randn(1, 1, 4, 4)
dropout_layer = torch.nn.Dropout2d(p=0.5, inplace=False)
output = dropout_layer(input_data)
print(input_data)
print(output)