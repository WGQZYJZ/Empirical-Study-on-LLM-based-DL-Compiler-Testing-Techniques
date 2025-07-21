'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.constant_\ntorch.nn.init.constant_(tensor, val)\n'
import torch
tensor = torch.rand(2, 3)
print(tensor)
torch.nn.init.constant_(tensor, val=0.5)
print(tensor)