import torch
from torch import nn
from torch.autograd import Variable
dimension = 5
sobol_engine = torch.quasirandom.SobolEngine(dimension)