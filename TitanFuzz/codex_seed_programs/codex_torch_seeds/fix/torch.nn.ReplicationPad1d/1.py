'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
input_data = torch.ones(1, 1, 3)
print('Input data: ', input_data)
pad = torch.nn.ReplicationPad1d(2)
output = pad(input_data)
print('Output data: ', output)