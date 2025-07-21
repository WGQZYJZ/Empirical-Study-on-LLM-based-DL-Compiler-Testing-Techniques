'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import numpy as np
input_data = torch.randn(1, 3, 5, 5)
torch.nn.init.xavier_normal_(input_data)
print(input_data)
input_data = torch.randn(1, 3, 5, 5)
torch.nn.init.xavier_normal_(input_data, gain=0.5)
print(input_data)