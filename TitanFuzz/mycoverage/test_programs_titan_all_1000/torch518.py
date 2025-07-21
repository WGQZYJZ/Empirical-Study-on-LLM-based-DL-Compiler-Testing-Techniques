import torch
from torch import nn
from torch.autograd import Variable
inp = np.array([[1, 2, 3], [4, 5, 6]])
torch.overrides.is_tensor_like(inp)