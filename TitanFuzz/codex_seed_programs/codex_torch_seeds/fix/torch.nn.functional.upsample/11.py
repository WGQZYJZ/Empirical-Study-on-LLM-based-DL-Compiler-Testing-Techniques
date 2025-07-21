"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
from torch.nn.functional import upsample
import torch
from torch.autograd import Variable
from torch.nn.functional import upsample
input = Variable(torch.randn(1, 1, 3, 3))
output = upsample(input, scale_factor=2)
print(output)