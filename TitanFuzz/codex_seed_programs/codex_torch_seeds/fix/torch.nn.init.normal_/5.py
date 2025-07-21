'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
import numpy as np
data = torch.randn(2, 3)
print(data)
torch.nn.init.normal_(data, mean=0.0, std=1.0)
print(data)
data = torch.zeros(2, 3)
torch.nn.init.normal_(data, mean=0.0, std=1.0)
print(data)
data = torch.ones(2, 3)
torch.nn.init.normal_(data, mean=0.0, std=1.0)
print(data)