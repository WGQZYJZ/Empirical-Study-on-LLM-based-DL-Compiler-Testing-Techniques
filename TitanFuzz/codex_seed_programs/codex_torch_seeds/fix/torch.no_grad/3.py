'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.no_grad()\n'
import torch
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)
with torch.no_grad():
    y = (x * 2)
print(y)
print(x.requires_grad)
print(y.requires_grad)
print((x.grad is None))
print((y.grad is None))
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.no_grad\ntorch.set_grad_enabled(mode)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.ones(2, 2), requires_grad=True)