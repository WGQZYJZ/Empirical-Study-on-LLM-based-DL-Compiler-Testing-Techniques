import torch
from torch import nn
from torch.autograd import Variable
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
torch.Tensor.baddbmm(batch1, batch1, batch2, beta=0.5, alpha=0.5)