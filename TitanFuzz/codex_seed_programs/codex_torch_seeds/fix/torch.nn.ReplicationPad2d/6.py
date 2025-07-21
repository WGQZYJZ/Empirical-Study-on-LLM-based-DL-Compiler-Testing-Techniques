'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
import torch.nn as nn
input_data = torch.Tensor([[1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8]])
input_data = input_data.view(1, 1, 2, 8)
pad = nn.ReplicationPad2d(2)
output = pad(input_data)
print(output)