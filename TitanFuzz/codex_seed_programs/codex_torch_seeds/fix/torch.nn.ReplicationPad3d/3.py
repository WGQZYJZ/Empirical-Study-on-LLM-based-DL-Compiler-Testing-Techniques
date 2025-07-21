'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad3d\ntorch.nn.ReplicationPad3d(padding)\n'
import torch
import torch.nn as nn
input_tensor = torch.randn(3, 3, 3, 3, 3)
print('input_tensor:', input_tensor)
print('input_tensor.shape:', input_tensor.shape)
replication_pad3d = nn.ReplicationPad3d((1, 1, 1, 1, 1, 1))
output_tensor = replication_pad3d(input_tensor)
print('output_tensor:', output_tensor)
print('output_tensor.shape:', output_tensor.shape)