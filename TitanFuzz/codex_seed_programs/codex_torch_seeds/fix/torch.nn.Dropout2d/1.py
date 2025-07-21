'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
input_data = torch.Tensor(1, 1, 2, 2)
input_data[0][0][0][0] = 1
input_data[0][0][0][1] = 2
input_data[0][0][1][0] = 3
input_data[0][0][1][1] = 4
dropout2d = nn.Dropout2d(p=0.5)
print(dropout2d(input_data))