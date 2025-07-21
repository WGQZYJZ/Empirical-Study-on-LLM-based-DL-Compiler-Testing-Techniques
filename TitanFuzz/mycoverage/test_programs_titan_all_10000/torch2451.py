import torch
from torch import nn
from torch.autograd import Variable
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
x_tensor = torch.from_numpy(x)
result = torch.Tensor.arctan_(x_tensor)