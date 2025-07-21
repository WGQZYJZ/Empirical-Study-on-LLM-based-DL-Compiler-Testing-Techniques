'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch.nn import ReplicationPad1d
input_data = torch.arange(1, 5, dtype=torch.float).view(1, 1, 4)
print('Input data: ', input_data)
padding = 3
replication_pad1d = ReplicationPad1d(padding)
output = replication_pad1d(input_data)
print('Output: ', output)