import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
torch.Tensor.is_leaf(_input_tensor)