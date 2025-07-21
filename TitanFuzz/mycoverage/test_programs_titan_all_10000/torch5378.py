import torch
from torch import nn
from torch.autograd import Variable
real = torch.randn(2, 3)
imag = torch.randn(2, 3)
complex_tensor = torch.complex(real, imag)