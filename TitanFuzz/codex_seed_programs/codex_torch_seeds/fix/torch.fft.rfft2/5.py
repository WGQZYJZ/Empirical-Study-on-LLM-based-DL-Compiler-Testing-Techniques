'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.rfft2\ntorch.fft.rfft2(input, s=None, dim=(-2, -1), norm=None, *, out=None)\n'
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
import torch
import torch.nn.functional as F
from torch.autograd import Variable
import numpy as np
input = Variable(torch.randn(1, 1, 4, 4))
print('Input: ', input)
output = torch.fft.rfft2(input, s=None, dim=((- 2), (- 1)), norm=None)
print('Output: ', output)