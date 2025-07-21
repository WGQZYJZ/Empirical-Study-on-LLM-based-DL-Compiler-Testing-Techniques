import torch
from torch import nn
from torch.autograd import Variable
a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
c = torch.mul(torch.from_numpy(a), torch.from_numpy(b))