'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
from torch.autograd import Variable
import torch
x = torch.randn(5)
x = Variable(x, requires_grad=True)
y = torch.nn.Softplus()(x)
y.backward(torch.ones(5))
print(x)
print(y)
print(x.grad)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
from torch.autograd import Variable
import torch
x = torch.randn(5)
x = Variable(x, requires_grad=True)
y = torch.nn.Tanh()(x)