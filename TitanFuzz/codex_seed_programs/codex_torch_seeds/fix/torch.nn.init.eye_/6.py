'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.eye_\ntorch.nn.init.eye_(tensor)\n'
import torch
tensor = torch.randn(2, 3)
print(tensor)
torch.nn.init.eye_(tensor)
print(tensor)