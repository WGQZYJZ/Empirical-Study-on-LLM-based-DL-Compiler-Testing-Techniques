import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.rand(3, 3)
_result_tensor = torch.Tensor.tril(_input_tensor, diagonal=0)
_result_tensor = torch.tril(_input_tensor, diagonal=0)