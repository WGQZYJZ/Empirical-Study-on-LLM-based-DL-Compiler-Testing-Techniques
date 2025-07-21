import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 2, 3], [4, 5, 6]])
_input_tensor_2 = torch.tensor([[1, 2, 3], [4, 5, 6]])
torch.Tensor.copy_(_input_tensor, _input_tensor_2, non_blocking=False)