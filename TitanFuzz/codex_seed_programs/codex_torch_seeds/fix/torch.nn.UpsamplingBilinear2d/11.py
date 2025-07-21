'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
input = Variable(torch.Tensor([[[[1, 2, 3], [4, 5, 6], [7, 8, 9]]]]))
upsample = nn.UpsamplingBilinear2d(size=(3, 3), scale_factor=None)
output = upsample(input)
print(output)