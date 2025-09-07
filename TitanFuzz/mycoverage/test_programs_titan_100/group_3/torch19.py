import torch
from torch import nn
from torch.autograd import Variable
tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
torch.concat((tensor_1, tensor_2), 0)
torch.cat((tensor_1, tensor_2), 0)