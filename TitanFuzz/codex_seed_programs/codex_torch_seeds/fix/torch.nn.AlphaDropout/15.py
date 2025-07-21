'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.AlphaDropout\ntorch.nn.AlphaDropout(p=0.5, inplace=False)\n'
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable
x = Variable(torch.randn(10, 10))
dropout = nn.AlphaDropout(p=0.5)
y = dropout(x)
print('Input data:')
print(x)
print('Output data:')
print(y)