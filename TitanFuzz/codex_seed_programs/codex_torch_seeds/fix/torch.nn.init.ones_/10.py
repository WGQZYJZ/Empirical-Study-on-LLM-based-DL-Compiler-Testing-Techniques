'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
input_tensor = torch.randn(2, 3)
print(input_tensor)
torch.nn.init.ones_(input_tensor)
print(input_tensor)