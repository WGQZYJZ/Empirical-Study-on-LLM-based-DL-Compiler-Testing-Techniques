'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.seed\ntorch.seed()\n'
import torch
input_data = torch.randn(1, 1, 3, 3)
torch.seed()
print('Input data: ', input_data)
print('Seed: ', torch.initial_seed())
print('Result: ', torch.normal(input_data))
print('Result: ', torch.normal(input_data))
print('Result: ', torch.normal(input_data))