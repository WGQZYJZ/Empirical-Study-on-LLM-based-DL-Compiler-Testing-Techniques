import torch
from torch import nn
from torch.autograd import Variable
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.Tensor.addbmm_(batch1, batch1, batch2, alpha=0.5, beta=0.5)
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)