import torch
from torch import nn
from torch.autograd import Variable
input = np.random.randn(4, 4)
input = torch.from_numpy(input)
torch.isnan(input)