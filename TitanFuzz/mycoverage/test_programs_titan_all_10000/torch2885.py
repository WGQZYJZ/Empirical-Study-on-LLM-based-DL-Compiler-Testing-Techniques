import torch
from torch import nn
from torch.autograd import Variable
input = torch.rand(5, 4)
input_sobol = torch.quasirandom.SobolEngine(4).draw(5)