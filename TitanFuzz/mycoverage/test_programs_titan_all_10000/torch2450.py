import torch
from torch import nn
from torch.autograd import Variable
np.random.seed(0)
torch.use_deterministic_algorithms(mode=True)
input_data = torch.rand(size=(2, 3), dtype=torch.float32, device='cpu')
torch.use_deterministic_algorithms(mode=True)
tensor = torch.rand(size=(2, 3), dtype=torch.float32, device='cpu')
tensor = torch.rand(size=(2, 3), dtype=torch.float32, device='cpu')