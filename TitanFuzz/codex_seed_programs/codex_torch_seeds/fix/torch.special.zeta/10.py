'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.zeta\ntorch.special.zeta(input, other, *, out=None)\n'
import torch
print('Task 1: import PyTorch')
print('Task 2: Generate input data')
print('Task 3: Call the API torch.special.zeta')
input = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([4.0, 5.0, 6.0])
torch.special.zeta(input, other)
input = torch.tensor([1.0, 2.0, 3.0])
other = torch.tensor([4.0, 5.0, 6.0])
torch.special.zeta(input, other, out=torch.empty(3))