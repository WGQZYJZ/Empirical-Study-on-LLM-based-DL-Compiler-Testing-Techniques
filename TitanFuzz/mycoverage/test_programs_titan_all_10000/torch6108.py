import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(3, 3, 3, 3)
lrn = torch.nn.LocalResponseNorm(size=3, alpha=0.0001, beta=0.75, k=1.0)
output_data = lrn(input_data)