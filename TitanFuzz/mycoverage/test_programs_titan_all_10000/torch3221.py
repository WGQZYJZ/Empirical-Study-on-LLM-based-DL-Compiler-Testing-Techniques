import torch
from torch import nn
from torch.autograd import Variable
data = np.arange(0, 10)
sampler = torch.utils.data.RandomSampler(data, replacement=False, num_samples=None, generator=None)