'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ReplicationPad2d\ntorch.nn.ReplicationPad2d(padding)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.Tensor(1, 1, 3, 3)
input_data[0, 0, :, :] = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
pad = nn.ReplicationPad2d(1)
output = pad(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ZeroPad2d\ntorch.nn.ZeroPad2d(padding)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.Tensor(1, 1, 3, 3)