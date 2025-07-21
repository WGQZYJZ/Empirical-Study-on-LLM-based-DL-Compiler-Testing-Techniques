import torch
from torch import nn
from torch.autograd import Variable
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x = torch.from_numpy(x)
y = torch.special.i0e(x)