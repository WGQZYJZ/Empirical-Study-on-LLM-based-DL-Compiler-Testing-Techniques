import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(3, 5)
_output_tensor = torch.Tensor.new_full(_input_tensor, 3, fill_value=10)