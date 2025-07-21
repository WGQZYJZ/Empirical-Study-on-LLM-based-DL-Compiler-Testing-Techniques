import torch
from torch import nn
from torch.autograd import Variable
n = torch.tensor(5, dtype=torch.int64)
d = torch.tensor(1.0, dtype=torch.float64)
output = torch.fft.fftfreq(n, d, out=None, dtype=None, layout=torch.strided, device=None, requires_grad=False)