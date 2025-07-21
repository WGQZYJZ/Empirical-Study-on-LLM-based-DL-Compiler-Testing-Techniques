'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.initial_seed\ntorch.initial_seed()\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
torch.initial_seed()
print(input_data)