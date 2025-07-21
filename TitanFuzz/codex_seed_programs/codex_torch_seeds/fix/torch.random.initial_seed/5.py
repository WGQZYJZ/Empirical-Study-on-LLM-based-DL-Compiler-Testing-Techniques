'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.random.initial_seed\ntorch.random.initial_seed()\n'
import torch
input_data = torch.rand(3, 3)
torch.random.initial_seed()
print(input_data)