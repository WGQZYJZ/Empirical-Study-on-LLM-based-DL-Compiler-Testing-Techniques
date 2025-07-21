'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.xavier_uniform_\ntorch.nn.init.xavier_uniform_(tensor, gain=1.0)\n'
import torch
from torch.nn import init
x = torch.empty(2, 2)
init.xavier_uniform_(x)
print(x)