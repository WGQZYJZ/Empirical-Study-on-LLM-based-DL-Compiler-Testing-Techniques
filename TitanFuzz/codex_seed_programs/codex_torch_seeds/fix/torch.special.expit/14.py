'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.expit\ntorch.special.expit(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 1.0, 2.0])
y = torch.special.expit(x)
print('The output of the API torch.special.expit is {}'.format(y))