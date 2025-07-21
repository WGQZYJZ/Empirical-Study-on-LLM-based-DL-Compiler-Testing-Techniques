'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad1d\ntorch.nn.ReplicationPad1d(padding)\n'
import torch
from torch import nn
input = torch.ones(1, 1, 2)
print(input)
pad = nn.ReplicationPad1d(padding=1)
output = pad(input)
print(output)