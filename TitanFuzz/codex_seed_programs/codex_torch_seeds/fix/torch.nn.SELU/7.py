'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.SELU\ntorch.nn.SELU(inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(2, 2))
print('Input data: ', x)
selu = torch.nn.SELU(inplace=False)
y = selu(x)
print('Output data: ', y)