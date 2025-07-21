'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmin\ntorch.nn.Softmin(dim=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
print('input:', input)
output = torch.nn.Softmin(dim=1)(input)
print('output:', output)