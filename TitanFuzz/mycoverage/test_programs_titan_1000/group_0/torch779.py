import torch
from torch import nn
from torch.autograd import Variable
real = torch.randn(4, 4)
imag = torch.randn(4, 4)
out = torch.complex(real, imag)