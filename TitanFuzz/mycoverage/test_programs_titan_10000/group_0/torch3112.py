import torch
from torch import nn
from torch.autograd import Variable

real = torch.randn(1, 3, 4, 5)
imag = torch.randn(1, 3, 4, 5)
result = torch.complex(real, imag)