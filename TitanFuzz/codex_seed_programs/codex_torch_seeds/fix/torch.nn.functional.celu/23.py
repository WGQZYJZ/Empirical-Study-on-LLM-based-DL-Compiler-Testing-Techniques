'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.celu\ntorch.nn.functional.celu(input, alpha=1., inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = Variable(torch.rand(5, 5))
F.celu(x, alpha=1.0, inplace=False)