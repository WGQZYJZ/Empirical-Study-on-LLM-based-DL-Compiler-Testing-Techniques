"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import torch
import torch.nn.functional as F
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 4, 4))
print('input: ', input)
upsample = F.upsample(input, scale_factor=2, mode='nearest')
print('upsample: ', upsample)