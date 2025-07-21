'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax\ntorch.nn.Softmax(dim=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(2, 3))
print('Input data: ', x)
softmax = torch.nn.Softmax(dim=1)
result = softmax(x)
print('Result: ', result)