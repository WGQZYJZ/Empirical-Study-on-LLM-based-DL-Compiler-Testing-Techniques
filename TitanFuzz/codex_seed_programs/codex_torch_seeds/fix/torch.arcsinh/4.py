'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.arcsinh\ntorch.arcsinh(input, *, out=None)\n'
import torch
x = torch.tensor([(- 1.0), 0.0, 1.0])
y = torch.arcsinh(x)
print('The result of torch.arcsinh is: ', y)