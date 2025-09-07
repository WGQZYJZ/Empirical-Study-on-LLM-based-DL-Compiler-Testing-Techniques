import torch
from torch import nn
from torch.autograd import Variable
real = torch.randn(2, 3, 4)
imag = torch.randn(2, 3, 4)
complex = torch.complex(real, imag)