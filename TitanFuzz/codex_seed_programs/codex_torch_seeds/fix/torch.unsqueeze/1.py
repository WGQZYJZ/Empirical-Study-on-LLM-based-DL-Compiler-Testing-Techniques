'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.unsqueeze\ntorch.unsqueeze(input, dim)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.Tensor([[1, 2, 3], [4, 5, 6]])
print('x:')
print(x)
y = torch.unsqueeze(x, dim=0)
print('y:')
print(y)