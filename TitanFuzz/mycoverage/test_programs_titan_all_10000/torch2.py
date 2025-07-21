import torch
from torch import nn
from torch.autograd import Variable
real_data = torch.randn(2, 3)
imag_data = torch.randn(2, 3)
complex_data = torch.complex(real_data, imag_data)