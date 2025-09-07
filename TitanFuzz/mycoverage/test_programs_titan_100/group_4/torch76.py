import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4)
torch.Tensor.fmod_(_input_tensor, 2)
torch.Tensor.fmod_(_input_tensor, 3)
torch.Tensor.fmod_(_input_tensor, 4)
torch.Tensor.fmod_(_input_tensor, 5)