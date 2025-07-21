'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nonzero\ntorch.nonzero(input, *, out=None, as_tuple=False)\n'
import torch
x = torch.tensor([[0.2, 0.3, 0.2, 0.9], [0.1, 0.2, 0.3, 0.4], [0.1, 0.1, 0.2, 0.7]])
y = torch.nonzero(x)
print('The input tensor: \n', x)
print('The nonzero element indices: \n', y)