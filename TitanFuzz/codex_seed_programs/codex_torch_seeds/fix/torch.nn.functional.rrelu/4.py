'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
x = Variable(torch.randn(5, 5))
y = F.rrelu(x, lower=(1.0 / 8), upper=(1.0 / 3), training=False, inplace=False)
print(y)