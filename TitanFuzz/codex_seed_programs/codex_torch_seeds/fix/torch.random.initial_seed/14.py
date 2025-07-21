'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.initial_seed\ntorch.random.initial_seed()\n'
import torch
input_data = torch.rand(10, 3)
print('Input Data: ', input_data)
torch.random.initial_seed()
print('Random Seed: ', torch.random.initial_seed())