'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.cos\ntorch.cos(input, *, out=None)\n'
import torch
input = torch.tensor([[(- 1.0), 0.0, 1.0], [2.0, 3.0, 4.0], [5.0, 6.0, 7.0], [8.0, 9.0, 10.0], [11.0, 12.0, 13.0]])
print('Input data: \n', input)
output = torch.cos(input)
print('Output data: \n', output)