'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
input_data = torch.arange(1, 7, dtype=torch.float32).view(1, 1, 6)
print('Input data: \n', input_data)
padding = 3
output = torch.nn.ReplicationPad1d(padding)(input_data)
print('Output data: \n', output)