import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(20, 5, 10, 10)
running_mean = torch.randn(5)
running_var = torch.randn(5)
input = torch.randn(20, 5, 10, 10)
running_mean = torch.randn(5)
running_var = torch.randn(5)
output = torch.nn.functional.batch_norm(input, running_mean, running_var, training=True)