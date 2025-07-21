'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout\ntorch.nn.Dropout(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.ones(2, 2))
print(x)
y = torch.nn.Dropout(p=0.5)
z = y(x)
print(z)