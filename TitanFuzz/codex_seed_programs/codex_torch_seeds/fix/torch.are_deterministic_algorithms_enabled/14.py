'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.are_deterministic_algorithms_enabled\ntorch.are_deterministic_algorithms_enabled()\n'
import torch
data = torch.rand(10)
print('Input data: ', data)
print('Algorithms enabled: ', torch.are_deterministic_algorithms_enabled())