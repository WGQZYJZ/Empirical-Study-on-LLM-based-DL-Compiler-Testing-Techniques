import torch
from torch import nn
from torch.autograd import Variable

x = np.random.rand(10)
x_tensor = torch.tensor(x)
torch.random.seed()