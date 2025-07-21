import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn((3, 3))
_input_tensor_1 = torch.ones((3, 3))
_input_tensor_2 = torch.zeros((3, 3))
_output_tensor_1 = torch.Tensor.all(_input_tensor, dim=None, keepdim=False)
_output_tensor_2 = torch.Tensor.all(_input_tensor, dim=0, keepdim=False)
_output_tensor_3 = torch.Tensor.all(_input_tensor, dim=1, keepdim=False)
_output_tensor_4 = torch.Tensor.all(_input_tensor, dim=None, keepdim=True)
_output_tensor_5 = torch.Tensor.all(_input_tensor, dim=0, keepdim=True)