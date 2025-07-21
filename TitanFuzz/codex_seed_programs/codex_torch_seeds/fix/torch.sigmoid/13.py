'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sigmoid\ntorch.sigmoid(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 1.0, 2.0])
print('The input data: \n', x)
y = torch.sigmoid(x)
print('The output data: \n', y)