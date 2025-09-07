import torch
from torch import nn
from torch.autograd import Variable

x = np.arange(0, (2 * np.pi), 0.1)
y = torch.fft.rfftfreq(x.shape[(- 1)], d=0.1)