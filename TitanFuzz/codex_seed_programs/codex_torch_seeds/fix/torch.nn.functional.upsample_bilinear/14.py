'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_bilinear\ntorch.nn.functional.upsample_bilinear(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F
input_data = Variable(torch.randn(1, 1, 2, 2))
print('Input data: ', input_data)
output_data = F.upsample_bilinear(input_data, scale_factor=2)
print('Output data: ', output_data)