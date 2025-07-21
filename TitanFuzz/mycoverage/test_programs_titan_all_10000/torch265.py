import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1, 3, 3, 3, 1, 2, 2, 3, 1, 2], [4, 4, 4, 4, 4, 4, 4, 4, 4, 4]])
_output_tensor = torch.Tensor.unique(_input_tensor, sorted=True, return_inverse=False, return_counts=False, dim=None)