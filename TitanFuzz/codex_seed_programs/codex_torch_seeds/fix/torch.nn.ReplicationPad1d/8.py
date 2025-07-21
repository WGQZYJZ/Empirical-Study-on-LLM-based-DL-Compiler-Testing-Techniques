'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
import torch.nn as nn
input_data = torch.arange(1, 11, dtype=torch.float)
input_data = input_data.view(1, 1, 10)
padding = nn.ReplicationPad1d(2)
output = padding(input_data)
print('Input: ', input_data)
print('Output: ', output)