'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout2d\ntorch.nn.Dropout2d(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.ones(1, 1, 4, 4))
print(x)
dropout = torch.nn.Dropout2d(p=0.5, inplace=False)
y = dropout(x)
print(y)
print(y)