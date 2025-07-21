'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import torch.nn as nn
import torch
import torch.nn as nn
input_data = torch.randn(3, 5)
nn.init.xavier_normal_(input_data)
print(input_data)