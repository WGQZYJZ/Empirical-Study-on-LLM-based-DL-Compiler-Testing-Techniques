import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.map_(_input_tensor, _input_tensor, (lambda x: (x * 2)))
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])