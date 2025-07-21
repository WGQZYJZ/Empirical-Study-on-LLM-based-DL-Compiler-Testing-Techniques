'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 1, 3, 3))
print(x)
dropout2d = torch.nn.Dropout2d(p=0.5, inplace=False)
y = dropout2d(x)
print(y)