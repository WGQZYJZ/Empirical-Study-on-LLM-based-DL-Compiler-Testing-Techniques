'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.alpha_dropout\ntorch.nn.functional.alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 10))
print('input: ', input)
output = torch.nn.functional.alpha_dropout(input, p=0.5, training=True)
print('output: ', output)