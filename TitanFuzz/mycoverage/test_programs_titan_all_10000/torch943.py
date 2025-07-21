import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[(- 0.5), 0.5, 0.5, (- 0.5)], [0.5, (- 0.5), 0.5, (- 0.5)], [0.5, 0.5, (- 0.5), (- 0.5)], [(- 0.5), (- 0.5), (- 0.5), (- 0.5)]])
torch.Tensor.ge_(input_tensor, 0)