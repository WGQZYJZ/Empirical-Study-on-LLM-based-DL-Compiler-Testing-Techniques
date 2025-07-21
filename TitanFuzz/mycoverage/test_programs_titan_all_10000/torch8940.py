import torch
from torch import nn
from torch.autograd import Variable
dim = 5
sobol_engine = torch.quasirandom.SobolEngine(dim)