import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
output = torch.nn.functional.kl_div(input, target)
output.backward(retain_graph=True)