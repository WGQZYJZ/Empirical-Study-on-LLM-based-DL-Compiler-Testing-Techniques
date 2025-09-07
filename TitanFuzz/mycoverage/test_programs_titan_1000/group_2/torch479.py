import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[True, False], [False, True]], dtype=torch.bool)
other = torch.tensor([[False, True], [True, False]], dtype=torch.bool)
torch.Tensor.logical_xor_(_input_tensor, other)