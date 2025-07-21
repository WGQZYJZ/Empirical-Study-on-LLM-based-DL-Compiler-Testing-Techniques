'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.initial_seed\ntorch.random.initial_seed()\n'
import torch
x = torch.rand(5, 3)
print(x)
torch.random.initial_seed()
print(torch.rand(5, 3))
torch.random.manual_seed(1)
print(torch.rand(5, 3))