import torch
from torch import nn
from torch.autograd import Variable
dimension = 3
scramble = False
seed = None
sobol_engine = torch.quasirandom.SobolEngine(dimension, scramble, seed)