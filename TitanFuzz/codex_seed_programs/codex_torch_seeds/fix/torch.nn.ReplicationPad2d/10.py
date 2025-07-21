'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
from torch.nn import ReplicationPad2d
input = torch.randn(1, 1, 4, 4)
print('Input: ', input)
padding = (1, 1, 1, 1)
print('Padding: ', padding)
padding_layer = ReplicationPad2d(padding)
output = padding_layer(input)
print('Output: ', output)