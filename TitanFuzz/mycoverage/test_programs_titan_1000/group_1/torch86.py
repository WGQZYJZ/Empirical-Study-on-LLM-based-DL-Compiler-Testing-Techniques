import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.Tensor([[[[1, 2, 1, 4], [2, 4, 2, 1], [1, 2, 4, 1], [2, 1, 1, 2]]]]))
lrn = torch.nn.LocalResponseNorm(2, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input_data)