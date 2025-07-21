"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import numpy as np
input_data = torch.randn(1, 1, 4, 4)
print('Input data: ', input_data)
upsample = nn.Upsample(scale_factor=2, mode='nearest')
output = upsample(Variable(input_data))
print('Output: ', output.data)