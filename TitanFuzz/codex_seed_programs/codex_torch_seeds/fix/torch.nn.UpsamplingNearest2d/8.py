'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch
input = torch.Tensor(1, 1, 4, 4)
input[0, 0, :, :] = torch.arange(0, 16).view(4, 4)
upsample_nearest = nn.UpsamplingNearest2d(scale_factor=2)
output = upsample_nearest(Variable(input))
print(output.data.numpy())