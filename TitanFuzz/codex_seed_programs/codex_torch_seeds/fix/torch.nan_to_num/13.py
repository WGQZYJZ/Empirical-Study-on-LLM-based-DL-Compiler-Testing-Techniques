'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nan_to_num\ntorch.nan_to_num(input, nan=0.0, posinf=None, neginf=None, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.FloatTensor([float('nan'), float('inf'), float('-inf'), 0]), requires_grad=True)
print('x = ', x)
y = torch.nan_to_num(x)
print('y = ', y)