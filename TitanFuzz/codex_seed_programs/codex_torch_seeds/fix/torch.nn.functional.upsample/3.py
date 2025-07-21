"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
from torch.nn import functional as F
input = Variable(torch.randn(1, 1, 4, 4))
output = F.upsample(input, size=None, scale_factor=2, mode='nearest', align_corners=None)
print(output)