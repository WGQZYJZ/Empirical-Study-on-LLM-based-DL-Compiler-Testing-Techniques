'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(2, 3))
y = torch.nn.functional.elu(x, alpha=1.0, inplace=False)
print(x)
print(y)
print(y.data[0][0])
print(y.data[0][1])
print(y.data[0][2])
print(y.data[1][0])
print(y.data[1][1])
print(y.data[1][2])