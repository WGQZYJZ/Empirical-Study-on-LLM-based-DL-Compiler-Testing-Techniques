import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
index = torch.tensor([[0, 1, 2], [1, 2, 0]])
tensor2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.index_add(input_tensor, dim=0, index=index, tensor2=tensor2)