"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample\ntorch.nn.functional.upsample(input, size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
input_data = Variable(torch.rand(1, 1, 4, 4))
upsample_data = F.upsample(input_data, size=(8, 8), mode='bilinear')
print(upsample_data)