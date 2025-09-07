import torch
from torch import nn
from torch.autograd import Variable
real = torch.tensor([math.pi, math.e])
imag = torch.tensor([math.pi, math.e])
out = torch.complex(real, imag)