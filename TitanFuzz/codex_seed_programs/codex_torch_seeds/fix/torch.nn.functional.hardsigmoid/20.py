'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.hardsigmoid\ntorch.nn.functional.hardsigmoid(input, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.randn(1, 1, 3, 3))
y = torch.nn.functional.hardsigmoid(x)
print(y)
print(y)