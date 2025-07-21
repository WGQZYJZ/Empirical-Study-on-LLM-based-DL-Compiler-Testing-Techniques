'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
import numpy as np
from torch.autograd import Variable
import torch
import numpy as np
from torch.autograd import Variable
input = Variable(torch.randn(2, 1, 2, 2), requires_grad=True)
output = torch.fft.irfftn(input)
print(output)