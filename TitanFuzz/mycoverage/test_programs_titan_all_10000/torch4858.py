import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[(- 2), (- 1), 0, 1, 2]], dtype=torch.float32)
torch.Tensor.sign_(input_tensor)