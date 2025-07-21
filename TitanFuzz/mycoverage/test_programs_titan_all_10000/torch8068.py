import torch
from torch import nn
from torch.autograd import Variable
input_data = Variable(torch.randn(1, 4, 3, 3, 3))
norm = torch.nn.InstanceNorm3d(4)
output_data = norm(input_data)