'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.UpsamplingBilinear2d\ntorch.nn.UpsamplingBilinear2d(size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
upsample = torch.nn.UpsamplingBilinear2d(scale_factor=2)
output = upsample(input)
print(input)
print(output)