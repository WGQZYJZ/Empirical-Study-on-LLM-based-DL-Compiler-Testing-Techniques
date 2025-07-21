'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.trace\ntorch.trace(input)\n'
import torch
input = torch.randn(3, 3)
print('Input Data: ')
print(input)
print('Output Data: ')
print(torch.trace(input))