import torch
from torch import nn
from torch.autograd import Variable
batch_size = 2
input_tensor = torch.empty(batch_size, 3, 4)
batch1 = torch.empty(batch_size, 3, 2)
batch2 = torch.empty(batch_size, 2, 4)
torch.Tensor.baddbmm_(input_tensor, batch1, batch2)