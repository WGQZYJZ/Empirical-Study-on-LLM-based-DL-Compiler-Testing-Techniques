import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(4, 4)
_output_tensor = torch.Tensor.new_full(_input_tensor, size=[2, 2], fill_value=10)