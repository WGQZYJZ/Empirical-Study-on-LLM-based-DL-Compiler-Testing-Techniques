'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Tanh\ntorch.nn.Tanh()\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 3))
print(x)
y = torch.nn.Tanh()
z = y(x)
print(z)