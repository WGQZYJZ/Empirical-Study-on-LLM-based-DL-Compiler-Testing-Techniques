import torch
from torch import nn
from torch.autograd import Variable
tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_2 = torch.tensor([[1, 1, 1], [2, 2, 2]])
result = torch.broadcast_tensors(tensor_1, tensor_2)
assert (result[0] == tensor_1).all()
assert (result[1] == tensor_2).all()