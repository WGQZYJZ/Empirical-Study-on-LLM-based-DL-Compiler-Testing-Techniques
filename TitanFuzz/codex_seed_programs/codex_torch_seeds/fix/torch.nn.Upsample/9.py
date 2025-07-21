"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 3, 3))
print('input: ', input)
upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
print('upsample: ', upsample)
output = upsample(input)
print('output: ', output)