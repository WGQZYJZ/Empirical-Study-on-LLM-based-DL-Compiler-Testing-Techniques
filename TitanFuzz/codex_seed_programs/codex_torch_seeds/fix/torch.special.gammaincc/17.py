'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.gammaincc\ntorch.special.gammaincc(input, other, *, out=None)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(4, 4))
other = Variable(torch.randn(4, 4))
output = torch.special.gammaincc(input, other)
print('The output of gammaincc is: ', output)