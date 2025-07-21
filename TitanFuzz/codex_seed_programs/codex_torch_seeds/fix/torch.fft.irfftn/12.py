'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.fft.irfftn\ntorch.fft.irfftn(input, s=None, dim=None, norm=None, *, out=None)\n'
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(4, 4, 4))
print(torch.fft.irfftn(input_data, 3))