'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.initial_seed\ntorch.initial_seed()\n'
import torch
x = torch.rand(10000, 1)
y = torch.rand(10000, 1)
torch.initial_seed()
z = (x + y)
print(z)