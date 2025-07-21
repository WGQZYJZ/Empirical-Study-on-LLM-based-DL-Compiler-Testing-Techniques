'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.ones_\ntorch.nn.init.ones_(tensor)\n'
import torch
input_tensor = torch.randn(4, 3)
print('Input data:\n', input_tensor)
torch.nn.init.ones_(input_tensor)
print('\nAfter calling torch.nn.init.ones_:\n', input_tensor)