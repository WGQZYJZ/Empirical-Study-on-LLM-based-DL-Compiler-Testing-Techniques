'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.RReLU\ntorch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.ones(2, 2), requires_grad=True)
print('Input data: x = {}'.format(x))
torch.nn.RReLU(lower=0.125, upper=0.3333333333333333, inplace=False)