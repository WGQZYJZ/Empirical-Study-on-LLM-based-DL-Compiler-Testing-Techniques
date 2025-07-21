import torch
from torch import nn
from torch.autograd import Variable
np.random.seed(0)
x = np.random.rand(2, 3)
torch.Generator(device='cpu')