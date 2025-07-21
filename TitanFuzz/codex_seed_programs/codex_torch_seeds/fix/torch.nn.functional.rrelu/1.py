'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu\ntorch.nn.functional.rrelu(input, lower=1./8, upper=1./3, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 2, 3, 4))
output = torch.nn.functional.rrelu(input)
print(output)