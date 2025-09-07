import torch
from torch import nn
from torch.autograd import Variable

data = np.arange(10)
sampler = torch.utils.data.Sampler(data)