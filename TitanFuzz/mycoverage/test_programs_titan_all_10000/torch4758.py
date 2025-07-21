import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = [[1, 2, 3], [4, 5, 6]]
data = torch.tensor([[1, 2, 3], [4, 5, 6]])
tensor = torch.Tensor.new_tensor(_input_tensor, data)