import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(np.array([(- 2.0), (- 1.0), 0.0, 1.0, 2.0, 3.0]))
y = torch.nn.Hardtanh(min_val=(- 1.0), max_val=1.0)(x)