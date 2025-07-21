import torch
from torch import nn
from torch.autograd import Variable
input = np.array([1, np.nan, np.inf])
input = torch.tensor(input)
output = torch.isfinite(input)