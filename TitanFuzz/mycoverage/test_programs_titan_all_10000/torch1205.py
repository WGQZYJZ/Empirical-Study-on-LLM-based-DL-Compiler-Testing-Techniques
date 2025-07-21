import torch
from torch import nn
from torch.autograd import Variable
real = torch.randn(1, 1)
imag = torch.randn(1, 1)
complex_tensor = torch.complex(real, imag)