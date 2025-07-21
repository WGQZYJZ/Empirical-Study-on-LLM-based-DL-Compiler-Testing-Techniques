import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
batch1 = torch.rand(2, 3, 4)
batch2 = torch.rand(2, 3, 4)
torch.Tensor.baddbmm_(input_tensor, batch1, batch2, beta=1, alpha=1)