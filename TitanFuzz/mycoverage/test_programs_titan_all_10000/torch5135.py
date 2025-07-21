import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(1, 3, 3, 3))
torch.nn.functional.local_response_norm(input, size=1, alpha=0.0001, beta=0.75, k=1.0)
input = Variable(torch.randn(1, 3))