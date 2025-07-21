import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor(np.random.rand(10, 10))
torch.Tensor.erfinv_(input_tensor)