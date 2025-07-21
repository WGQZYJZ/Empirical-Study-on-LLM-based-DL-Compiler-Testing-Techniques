'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
input_data = torch.ones(2, 2, requires_grad=True)
dropout_layer = torch.nn.Dropout2d(p=0.5, inplace=False)
print('Input data: ', input_data)
print('Output data: ', dropout_layer(input_data))