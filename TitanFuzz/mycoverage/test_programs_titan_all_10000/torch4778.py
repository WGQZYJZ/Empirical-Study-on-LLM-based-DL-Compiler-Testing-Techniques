import torch
from torch import nn
from torch.autograd import Variable
real = torch.randn(3, 3)
imag = torch.randn(3, 3)
out = torch.complex(real, imag)