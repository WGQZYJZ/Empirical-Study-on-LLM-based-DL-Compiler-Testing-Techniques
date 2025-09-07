import torch
from torch import nn
from torch.autograd import Variable
A = np.random.rand(100, 100)
A = torch.from_numpy(A)
torch.lobpcg(A)