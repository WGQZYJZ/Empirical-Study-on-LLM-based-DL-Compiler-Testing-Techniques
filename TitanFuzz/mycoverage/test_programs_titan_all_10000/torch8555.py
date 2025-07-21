import torch
from torch import nn
from torch.autograd import Variable
A = torch.tensor([[12.0, (- 51.0), 4.0], [6.0, 167.0, (- 68.0)], [(- 4.0), 24.0, (- 41.0)]])
(q, r) = torch.linalg.qr(A)