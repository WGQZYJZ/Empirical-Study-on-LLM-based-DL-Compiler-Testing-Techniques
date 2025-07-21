'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.randn(2, 3)
print('Input data:')
print(input_data)
dropout_layer = nn.Dropout(p=0.5, inplace=False)
output_data = dropout_layer(input_data)
print('Output data:')
print(output_data)