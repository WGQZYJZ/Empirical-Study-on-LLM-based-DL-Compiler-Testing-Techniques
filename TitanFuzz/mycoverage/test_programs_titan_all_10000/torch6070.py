import torch
from torch import nn
from torch.autograd import Variable
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
sampler = torch.utils.data.RandomSampler(data, replacement=False, num_samples=5)
data = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])