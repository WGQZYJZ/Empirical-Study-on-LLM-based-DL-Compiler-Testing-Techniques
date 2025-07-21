import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(5, 5, 5, 5)
input_data = torch.randn(5, 5, 5, 5)
input_data = torch.randn(5, 5, 5, 5)
lrn = torch.nn.LocalResponseNorm(size=5, alpha=0.0001, beta=0.75, k=1.0)
output = lrn(input_data)