import torch
from torch import nn
from torch.autograd import Variable
batch_size = 3
num_features = 4
batch1 = torch.rand(batch_size, num_features)
batch2 = torch.rand(batch_size, num_features, num_features)
result = torch.Tensor.baddbmm(batch1, batch2, beta=1, alpha=1)