'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Hardshrink\ntorch.nn.Hardshrink(lambd=0.5)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([(- 2), (- 1), 0, 1, 2]))
hardshrink = torch.nn.Hardshrink(lambd=0.5)
y = hardshrink(x)
print(y.data)