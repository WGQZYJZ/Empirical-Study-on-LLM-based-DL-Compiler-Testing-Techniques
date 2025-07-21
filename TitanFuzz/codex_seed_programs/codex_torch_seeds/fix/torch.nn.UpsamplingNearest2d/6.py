'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
from torch.nn import UpsamplingNearest2d
import torch
input = torch.randn(1, 1, 5, 5)
upsample = UpsamplingNearest2d(scale_factor=2)
output = upsample(input)
print(output.size())
upsample = UpsamplingNearest2d(size=8)
output = upsample(input)
print(output.size())
upsample = UpsamplingNearest2d(scale_factor=2)
input = Variable(input)
output = upsample(input)
print(output.size())