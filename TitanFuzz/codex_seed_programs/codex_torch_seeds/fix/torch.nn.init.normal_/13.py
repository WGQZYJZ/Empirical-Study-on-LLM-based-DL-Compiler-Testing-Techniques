'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.normal_\ntorch.nn.init.normal_(tensor, mean=0.0, std=1.0)\n'
import torch
tensor = torch.empty(3, 3)
torch.nn.init.normal_(tensor, mean=0.0, std=1.0)
print(tensor)