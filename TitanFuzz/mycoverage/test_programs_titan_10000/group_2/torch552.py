import torch
from torch import nn
from torch.autograd import Variable

dimension = 3
torch.quasirandom.SobolEngine(dimension, scramble=False, seed=None)