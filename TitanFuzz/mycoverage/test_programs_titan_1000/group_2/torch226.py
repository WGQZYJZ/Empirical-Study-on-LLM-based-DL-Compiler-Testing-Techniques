import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4)
indices = torch.LongTensor([[0, 1], [2, 3]])
values = torch.FloatTensor([3, 4, 5, 6])
torch.Tensor.index_put(_input_tensor, indices, values, accumulate=False)