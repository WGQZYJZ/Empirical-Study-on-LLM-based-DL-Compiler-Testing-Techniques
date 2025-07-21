import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
torch.Tensor.is_sparse(_input_tensor)