'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
input = torch.randn(3, 3)
print('Input data: \n', input)
print('Input data type: ', input.type())
output = torch.sign(input)
print('\nOutput data: \n', output)
print('Output data type: ', output.type())