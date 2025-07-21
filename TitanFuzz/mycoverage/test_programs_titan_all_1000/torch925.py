import torch
from torch import nn
from torch.autograd import Variable
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
a = torch.from_numpy(a)
b = torch.from_numpy(b)
c = torch.clone(a)
d = torch.clone(b)