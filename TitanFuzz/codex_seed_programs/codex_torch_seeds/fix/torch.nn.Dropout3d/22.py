'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Dropout3d\ntorch.nn.Dropout3d(p=0.5, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.ones(1, 1, 2, 2, 2))
print('input: ', input)
output = torch.nn.Dropout3d(p=0.5, inplace=False)(input)
print('output: ', output)