'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Softmax2d\ntorch.nn.Softmax2d()\n'
import torch
from torch.autograd import Variable
from torch.nn import Softmax2d
input = Variable(torch.randn(1, 1, 3, 3))
print('Input: ', input)
softmax = Softmax2d()
output = softmax(input)
print('Output: ', output)