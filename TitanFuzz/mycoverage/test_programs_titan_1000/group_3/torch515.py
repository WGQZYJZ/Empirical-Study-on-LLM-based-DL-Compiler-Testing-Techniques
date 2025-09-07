import torch
from torch import nn
from torch.autograd import Variable
input = torch.randn(4, 4, 4, dtype=torch.double, requires_grad=True)
input_np = np.random.randn(4, 4, 4)
output = torch.fft.ifftn(input)