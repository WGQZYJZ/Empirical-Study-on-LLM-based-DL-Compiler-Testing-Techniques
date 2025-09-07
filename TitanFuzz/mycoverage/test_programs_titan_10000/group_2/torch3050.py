import torch
from torch import nn
from torch.autograd import Variable

x = np.linspace((- 1), 1, num=100)
x = torch.from_numpy(x)
y = torch.special.i0e(x)