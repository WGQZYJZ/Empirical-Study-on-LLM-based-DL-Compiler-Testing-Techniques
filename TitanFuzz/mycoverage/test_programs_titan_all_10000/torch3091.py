import torch
from torch import nn
from torch.autograd import Variable
x = torch.rand(2, 3, dtype=torch.float32)
torch.use_deterministic_algorithms(True)
torch.use_deterministic_algorithms(False)