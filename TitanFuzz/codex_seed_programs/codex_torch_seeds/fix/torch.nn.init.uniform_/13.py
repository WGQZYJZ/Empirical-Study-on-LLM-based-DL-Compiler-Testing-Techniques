'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
tensor = torch.empty(3, 3)
torch.nn.init.uniform_(tensor, a=0.0, b=1.0)
print(tensor)