'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.linalg.slogdet\ntorch.linalg.slogdet(A, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
A = Variable(torch.randn(2, 2), requires_grad=True)
print('A: ', A)
slogdet = torch.linalg.slogdet(A)
print('slogdet: ', slogdet)