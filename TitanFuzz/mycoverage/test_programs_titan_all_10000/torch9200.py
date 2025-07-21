import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([(- 3.1415), (- 3.1415), (- 3.1415), (- 3.1415)])
torch.Tensor.fmod_(input_tensor, 3.1415)