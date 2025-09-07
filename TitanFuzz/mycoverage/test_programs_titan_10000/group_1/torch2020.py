import torch
from torch import nn
from torch.autograd import Variable

input_data = np.random.rand(3, 3)
torch.Tensor.share_memory_(input_data)