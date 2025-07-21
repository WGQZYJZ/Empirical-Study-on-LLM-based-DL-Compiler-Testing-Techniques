import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.rand(2, 3, 4)
torch.Tensor.index_put_(input_tensor, torch.LongTensor([[0, 1, 2, 1], [1, 0, 1, 2]]), torch.FloatTensor([0, 1, 2, 3]), accumulate=False)