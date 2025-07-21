import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
mask = torch.tensor([[True, True, False], [False, True, True]])
_output = torch.Tensor.sparse_mask(_input_tensor, mask)