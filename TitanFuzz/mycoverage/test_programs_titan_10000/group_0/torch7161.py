import torch
from torch import nn
from torch.autograd import Variable

input_data = torch.tensor([[1, 1, 1], [1, 1, (- 1)], [1, (- 1), 1], [1, (- 1), (- 1)], [(- 1), 1, 1], [(- 1), 1, (- 1)], [(- 1), (- 1), 1], [(- 1), (- 1), (- 1)]])
result = torch.angle(input_data)