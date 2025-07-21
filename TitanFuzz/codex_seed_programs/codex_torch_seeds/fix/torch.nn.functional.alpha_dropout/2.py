'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.randn(3, 3))
print('Input data:')
print(x)
x_dropout = torch.nn.functional.alpha_dropout(x, p=0.5, training=False, inplace=False)
print('Output data:')
print(x_dropout)