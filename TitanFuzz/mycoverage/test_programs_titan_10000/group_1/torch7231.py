import torch
from torch import nn
from torch.autograd import Variable

dimension = 3
scramble = False
seed = None
torch.quasirandom.SobolEngine(dimension, scramble, seed)