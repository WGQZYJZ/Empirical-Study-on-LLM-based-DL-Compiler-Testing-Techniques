import torch
from torch import nn
from torch.autograd import Variable

input = np.array([[0, (np.pi / 2), np.pi, ((3 * np.pi) / 2), (2 * np.pi)]])
input = torch.from_numpy(input)
output = torch.cos(input)