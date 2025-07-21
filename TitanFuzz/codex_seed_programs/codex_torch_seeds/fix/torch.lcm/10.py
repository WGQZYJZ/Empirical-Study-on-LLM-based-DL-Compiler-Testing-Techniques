'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.lcm\ntorch.lcm(input, other, *, out=None)\n'
import torch
a = torch.tensor([2, 4, 6])
b = torch.tensor([6, 4, 2])
print('LCM of a and b is: ', torch.lcm(a, b))