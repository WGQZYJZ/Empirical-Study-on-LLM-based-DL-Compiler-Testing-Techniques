import torch
from torch import nn
from torch.autograd import Variable
batch1 = torch.rand(10, 3, 4)
batch2 = torch.rand(10, 4, 5)
torch.Tensor.addbmm_(batch1, batch1, batch2, beta=0.5, alpha=0.5)
torch.Tensor.addbmm_(batch1, batch1, batch2, beta=0.5, alpha=0.5)
torch.Tensor.addbmm_(batch1, batch1, batch2, beta=0.5, alpha=0.5)