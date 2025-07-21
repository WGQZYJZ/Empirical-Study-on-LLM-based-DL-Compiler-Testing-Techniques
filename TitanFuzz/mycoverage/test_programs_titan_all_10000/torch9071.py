import torch
from torch import nn
from torch.autograd import Variable
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)
result = torch.is_tensor(tensor)