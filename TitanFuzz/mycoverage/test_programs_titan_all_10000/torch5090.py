import torch
from torch import nn
from torch.autograd import Variable
input_tensor = np.array([[1, 2, 3], [4, 5, 6]])
input_tensor = torch.from_numpy(input_tensor)
torch.Tensor.t_(input_tensor)