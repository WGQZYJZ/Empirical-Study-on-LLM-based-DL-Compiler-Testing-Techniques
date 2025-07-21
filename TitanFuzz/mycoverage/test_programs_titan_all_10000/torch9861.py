import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor_repeat = torch.Tensor.repeat(input_tensor, 2, 0)