'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.init.dirac_\ntorch.nn.init.dirac_(tensor, groups=1)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 3, 3))
torch.nn.init.dirac_(input)
print(input)