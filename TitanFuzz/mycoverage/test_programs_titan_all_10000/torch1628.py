import torch
from torch import nn
from torch.autograd import Variable
batch1 = torch.randn(10, 3, 4)
batch2 = torch.randn(10, 4, 5)
result = torch.empty(10, 3, 5)
torch.Tensor.baddbmm_(result, batch1, batch2)