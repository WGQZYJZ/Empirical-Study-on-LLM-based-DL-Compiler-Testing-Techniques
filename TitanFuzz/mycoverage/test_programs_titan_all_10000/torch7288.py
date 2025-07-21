import torch
from torch import nn
from torch.autograd import Variable
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data)
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data, dtype=torch.float32)
data = [[1, 2, 3], [4, 5, 6]]
data = [[1, 2, 3], [4, 5, 6]]
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cpu'))
data = [[1, 2, 3], [4, 5, 6]]
data