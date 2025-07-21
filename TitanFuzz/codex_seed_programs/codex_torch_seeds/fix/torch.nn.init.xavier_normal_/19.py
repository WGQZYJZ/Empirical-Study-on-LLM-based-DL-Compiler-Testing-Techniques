'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import torch.nn as nn
input_tensor = torch.rand(10, 10)
nn.init.xavier_normal_(input_tensor)
print(input_tensor)