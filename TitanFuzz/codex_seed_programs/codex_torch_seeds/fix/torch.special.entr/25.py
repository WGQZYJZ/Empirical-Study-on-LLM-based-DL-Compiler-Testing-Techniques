'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.entr\ntorch.special.entr(input, *, out=None)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 5))
print(torch.special.entr(x))