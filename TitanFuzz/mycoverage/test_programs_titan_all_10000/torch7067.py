import torch
from torch import nn
from torch.autograd import Variable
vec1 = torch.tensor(np.random.rand(10), dtype=torch.float32)
vec2 = torch.tensor(np.random.rand(10), dtype=torch.float32)
out = torch.Tensor.outer(vec1, vec2)