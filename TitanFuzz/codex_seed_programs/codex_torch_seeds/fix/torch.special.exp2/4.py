'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.special.exp2\ntorch.special.exp2(input, *, out=None)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.rand(5, 3))
y = torch.special.exp2(x)
print(y)