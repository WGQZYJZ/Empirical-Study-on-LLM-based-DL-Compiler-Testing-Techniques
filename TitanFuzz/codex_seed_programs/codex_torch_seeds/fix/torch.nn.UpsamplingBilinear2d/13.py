'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input = Variable(torch.Tensor(1, 1, 4, 4).uniform_())
upsampling = nn.UpsamplingBilinear2d(size=(8, 8))
output = upsampling(input)
print(output.size())