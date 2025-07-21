import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.randn(20, 10)
softplus = torch.nn.Softplus(beta=1, threshold=20)
output = softplus(input_data)