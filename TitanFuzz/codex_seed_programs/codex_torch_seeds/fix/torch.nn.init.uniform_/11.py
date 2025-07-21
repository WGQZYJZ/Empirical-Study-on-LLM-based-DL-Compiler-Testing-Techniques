'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
print('Task 1: import PyTorch')
print(torch.__version__)
print('\nTask 2: Generate input data')
tensor = torch.rand(2, 3)
print(tensor)
print('\nTask 3: Call the API torch.nn.init.uniform_')
torch.nn.init.uniform_(tensor, a=0.0, b=1.0)
print(tensor)