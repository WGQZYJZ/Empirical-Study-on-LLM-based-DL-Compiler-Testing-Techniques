import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.Tensor(np.random.rand(3, 3))
(q, r) = torch.geqrf(input_data)