import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(1, 1, 5, 5)
input_data = torch.randn(1, 1, 5, 5)
norm_data = torch.nn.LocalResponseNorm(size=2, alpha=0.0001, beta=0.75, k=1.0)
output = norm_data(input_data)
input_data = torch.randn(1, 1, 5, 5)
input_data = torch.randn(1, 1, 5, 5)