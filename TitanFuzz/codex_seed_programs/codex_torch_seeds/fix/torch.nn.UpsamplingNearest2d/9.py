'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingNearest2d\ntorch.nn.UpsamplingNearest2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 5, 5))
upsample = torch.nn.UpsamplingNearest2d(scale_factor=2)
output = upsample(input)
print(output)