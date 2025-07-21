'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.xlogy\ntorch.special.xlogy(input, other, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.randn(4, 4), requires_grad=True)
y = Variable(torch.randn(4, 4), requires_grad=True)
z = torch.special.xlogy(x, y)
z.backward(torch.ones(4, 4))
print(x.grad.data)
print(y.grad.data)