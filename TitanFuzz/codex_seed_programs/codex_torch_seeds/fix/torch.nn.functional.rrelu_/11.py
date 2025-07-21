'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.rrelu_\ntorch.nn.functional.rrelu_(input, lower=1./8, upper=1./3, training=False)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 5, 5))
print(input)
print(torch.nn.functional.rrelu_(input))
print(torch.nn.functional.rrelu_(input, lower=0.2))
print(torch.nn.functional.rrelu_(input, upper=0.7))
print(torch.nn.functional.rrelu_(input, lower=0.2, upper=0.7))
print(torch.nn.functional.rrelu_(input, lower=0.2, upper=0.7, training=True))