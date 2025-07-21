import torch
from torch import nn
from torch.autograd import Variable
x = torch.tensor(np.random.rand(4, 4))
y = torch.nn.functional.tanh(x)