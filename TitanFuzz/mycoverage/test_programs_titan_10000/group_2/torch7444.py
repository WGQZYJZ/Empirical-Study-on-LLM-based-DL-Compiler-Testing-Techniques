import torch
from torch import nn
from torch.autograd import Variable

input = np.random.randn(2, 3)
output = torch.erf(torch.tensor(input))