import torch
from torch import nn
from torch.autograd import Variable
input = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
input = torch.from_numpy(input)
output = torch.special.i0e(input)