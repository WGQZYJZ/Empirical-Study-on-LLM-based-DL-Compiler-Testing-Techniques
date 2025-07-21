import torch
from torch import nn
from torch.autograd import Variable
a = np.array([1, 2, 3, 4, 5])
b = torch.from_numpy(a)
c = b.numpy()