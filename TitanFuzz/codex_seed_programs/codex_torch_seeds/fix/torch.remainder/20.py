'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.remainder\ntorch.remainder(input, other, *, out=None)\n'
import torch
input_data = torch.randn(3, 3)
print('Input data:\n', input_data)
remainder = torch.remainder(input_data, 2)
print('\nRemainder:\n', remainder)