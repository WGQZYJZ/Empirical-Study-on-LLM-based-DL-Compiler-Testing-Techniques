'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.sign\ntorch.sign(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), (- 0.5), 0.0, 0.5, 1.0])
y = torch.sign(x)
print('The result of torch.sign: ', y)