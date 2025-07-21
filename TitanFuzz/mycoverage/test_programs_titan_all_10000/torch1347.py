import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(10, 3, 3, 3)
running_mean = torch.rand(3)
running_var = torch.rand(3)
weight = torch.rand(3)
bias = torch.rand(3)
output = torch.nn.functional.batch_norm(input_data, running_mean, running_var, weight, bias, training=True, momentum=0.1, eps=1e-05)