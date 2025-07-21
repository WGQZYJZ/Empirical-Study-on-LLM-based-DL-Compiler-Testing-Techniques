'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import torch
input = Variable(torch.randn(1, 1, 3, 3))
output = F.upsample_nearest(input, scale_factor=2)
print(input)
print(output)