'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_normal_\ntorch.nn.init.xavier_normal_(tensor, gain=1.0)\n'
import torch
import numpy as np
import torch
input_size = 10
batch_size = 3
input_data = torch.randn(batch_size, input_size)
torch.nn.init.xavier_normal_(input_data)
print(input_data)