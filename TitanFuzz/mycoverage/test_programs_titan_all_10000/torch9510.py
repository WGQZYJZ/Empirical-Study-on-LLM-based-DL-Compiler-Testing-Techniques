import torch
from torch import nn
from torch.autograd import Variable
data = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
tensor = torch.Tensor(data)
torch.Tensor.renorm_(tensor, p=2, dim=0, maxnorm=2)