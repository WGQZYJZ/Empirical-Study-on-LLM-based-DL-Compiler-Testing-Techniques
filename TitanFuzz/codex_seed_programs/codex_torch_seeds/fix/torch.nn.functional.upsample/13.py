"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
from torch.nn.functional import upsample
input = Variable(torch.ones(1, 1, 5, 5))
print('Input:\n', input)
output = upsample(input, scale_factor=2, mode='nearest')
print('Output:\n', output)