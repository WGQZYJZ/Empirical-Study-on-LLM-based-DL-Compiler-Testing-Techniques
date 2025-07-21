'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
tensor = torch.ones(2, 2)
print(tensor)
torch.nn.init.ones_(tensor)
print(tensor)