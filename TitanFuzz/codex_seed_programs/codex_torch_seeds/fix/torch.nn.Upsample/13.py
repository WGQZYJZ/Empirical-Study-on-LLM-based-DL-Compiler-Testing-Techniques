"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(2, 2, 3, 3))
upsample = torch.nn.Upsample(scale_factor=2)
output = upsample(input)
print(output.size())
upsample = torch.nn.Upsample(size=(7, 7))
output = upsample(input)
print(output.size())
upsample = torch.nn.Upsample(size=(7, 7), mode='bilinear')
output = upsample(input)
print(output.size())