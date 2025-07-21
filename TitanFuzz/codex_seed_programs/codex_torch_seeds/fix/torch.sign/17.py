'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
input = torch.randn(4, 4)
print('Input Data')
print(input)
output = torch.sign(input)
print('Output Data')
print(output)