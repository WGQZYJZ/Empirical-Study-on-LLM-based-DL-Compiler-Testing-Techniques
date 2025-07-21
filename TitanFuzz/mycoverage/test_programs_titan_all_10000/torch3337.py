import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
result = torch.Tensor.not_equal(_input_tensor, other=5)