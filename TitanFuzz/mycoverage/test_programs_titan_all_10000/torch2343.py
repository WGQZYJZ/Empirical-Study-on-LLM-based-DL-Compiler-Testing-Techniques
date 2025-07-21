import torch
from torch import nn
from torch.autograd import Variable
data = [1, 2, 3, 4, 5]
tensor = torch.tensor(data)
tensor = torch.tensor(data, dtype=torch.float32)
tensor = torch.tensor(data, dtype=torch.float32, device=torch.device('cpu'))