import torch
from torch import nn
from torch.autograd import Variable
_input_tensor = torch.tensor([[(- np.pi), ((- np.pi) / 2), 0, (np.pi / 2), np.pi]])
torch.Tensor.sin_(_input_tensor)