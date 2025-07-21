import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([0, 1, (- 1), np.inf, (- np.inf)])
input_data = torch.from_numpy(input_data)
torch.arctan(input_data)