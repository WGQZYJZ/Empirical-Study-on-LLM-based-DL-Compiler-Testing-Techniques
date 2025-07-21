import torch
from torch import nn
from torch.autograd import Variable
tensor_a = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_b = torch.tensor([[7, 8, 9], [10, 11, 12]])
tensor_c = torch.tensor([[13, 14, 15], [16, 17, 18]])
tensor_concat = torch.concat((tensor_a, tensor_b, tensor_c), dim=1)