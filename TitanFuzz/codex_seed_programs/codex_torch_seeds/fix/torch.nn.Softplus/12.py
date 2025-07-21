'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softplus\ntorch.nn.Softplus(beta=1, threshold=20)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
print(x)
from torch.nn import Softplus
softplus_fn = Softplus()
y = softplus_fn(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Sigmoid\ntorch.nn.Sigmoid()\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
print(x)
from torch.nn import Sigmoid
sigmoid_fn = Sigmoid()
y = sigmoid_fn(x)
print(y)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch