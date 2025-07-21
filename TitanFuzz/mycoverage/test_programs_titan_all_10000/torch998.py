import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.rand(1, 3, 4, 4)
norm = torch.nn.LazyInstanceNorm2d(affine=True, track_running_stats=True)
output = norm(input_data)