import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.arange(0, 9, dtype=torch.float32).reshape(3, 3)
_output_tensor = torch.Tensor.as_strided(_input_tensor, size=(2, 2), stride=(3, 3))