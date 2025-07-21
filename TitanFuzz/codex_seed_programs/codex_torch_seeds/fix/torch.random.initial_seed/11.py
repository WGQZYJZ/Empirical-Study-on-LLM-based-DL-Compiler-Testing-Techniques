'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.initial_seed\ntorch.random.initial_seed()\n'
import torch
input = torch.randn(2, 3)
print(input)
torch.random.initial_seed()
print(input)