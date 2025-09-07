import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.index_put_(input_tensor, torch.LongTensor([[0, 0], [1, 1], [2, 2]]), torch.Tensor([[10, 20, 30], [40, 50, 60], [70, 80, 90]]), accumulate=False)