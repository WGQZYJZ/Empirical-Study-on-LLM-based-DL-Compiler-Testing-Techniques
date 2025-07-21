"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch import nn
from torch.autograd import Variable
input = Variable(torch.rand(1, 1, 4, 4))
print(input)
input = Variable(torch.rand(1, 1, 4, 4))
print(input)
output = nn.functional.upsample(input, size=(8, 8), mode='bilinear')
print(output)