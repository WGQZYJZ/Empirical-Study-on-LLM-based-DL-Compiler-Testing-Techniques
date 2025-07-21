'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.psi\ntorch.special.psi(input, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), requires_grad=True)
y = torch.special.psi(x)
print(y)