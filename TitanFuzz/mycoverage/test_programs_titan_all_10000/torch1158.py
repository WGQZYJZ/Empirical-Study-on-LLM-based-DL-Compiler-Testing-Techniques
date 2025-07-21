import torch
from torch import nn
from torch.autograd import Variable
input_tensor_1 = torch.tensor([[1, 2, 3], [4, 5, 6]])
input_tensor_2 = torch.tensor([[7, 8, 9], [10, 11, 12]])
torch.Tensor.put_(input_tensor_1, torch.tensor([0, 1]), input_tensor_2, accumulate=False)