import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, requires_grad=True)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)
output.backward(torch.ones(4, 4))
output = torch.nn.functional.softplus(input, beta=1, threshold=20)
output.backward(torch.ones(4, 4))