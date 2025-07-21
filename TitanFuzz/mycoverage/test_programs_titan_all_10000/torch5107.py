import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
other = torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]]))
torch.Tensor.bitwise_left_shift_(input_tensor, other)