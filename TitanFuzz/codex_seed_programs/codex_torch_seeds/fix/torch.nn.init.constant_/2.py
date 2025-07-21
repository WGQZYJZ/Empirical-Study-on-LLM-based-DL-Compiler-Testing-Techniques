'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
data = torch.ones(2, 2)
print(data)
torch.nn.init.constant_(data, val=3)
print(data)