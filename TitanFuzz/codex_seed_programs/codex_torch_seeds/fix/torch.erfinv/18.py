'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.erfinv\ntorch.erfinv(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
print('The input data is:')
print(x)
y = torch.erfinv(x)
print('The output data is:')
print(y)