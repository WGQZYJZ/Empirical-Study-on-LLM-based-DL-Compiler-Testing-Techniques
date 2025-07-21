'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
import torch.nn as nn
import torch
input_data = torch.randn(1, 1, 4, 4)
padding_size = 2
padding = (padding_size, padding_size, padding_size, padding_size)
replication_pad = nn.ReplicationPad2d(padding)
output = replication_pad(input_data)
print(input_data)
print(output)