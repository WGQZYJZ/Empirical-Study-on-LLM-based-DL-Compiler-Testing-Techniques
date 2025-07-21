'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
input = torch.randn(1, 1, 3, 3)
padding = (1, 2, 1, 2)
output = torch.nn.ReplicationPad2d(padding)(input)
print(output)