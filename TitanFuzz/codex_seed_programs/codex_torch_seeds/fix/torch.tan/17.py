'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.tan\ntorch.tan(input, *, out=None)\n'
import torch
data = torch.tensor([(- 1), 0, 1])
print('Input data: ', data)
out = torch.tan(data)
print('Output data: ', out)