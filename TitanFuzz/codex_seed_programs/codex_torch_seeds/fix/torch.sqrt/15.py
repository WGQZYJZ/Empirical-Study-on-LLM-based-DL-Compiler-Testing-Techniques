'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sqrt\ntorch.sqrt(input, *, out=None)\n'
import torch
input_data = torch.randn(1, 3)
sqrt_data = torch.sqrt(input_data)
print('Input data:')
print(input_data)
print('Sqrt data:')
print(sqrt_data)