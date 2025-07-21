'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.uniform_\ntorch.nn.init.uniform_(tensor, a=0.0, b=1.0)\n'
import torch
data = torch.randn(2, 3)
print('Input data:')
print(data)
torch.nn.init.uniform_(data, a=0.0, b=1.0)
print('Output data:')
print(data)