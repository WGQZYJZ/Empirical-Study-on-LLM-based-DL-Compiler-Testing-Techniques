import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3, 224, 224)
torch.Tensor.to_mkldnn(_input_tensor)