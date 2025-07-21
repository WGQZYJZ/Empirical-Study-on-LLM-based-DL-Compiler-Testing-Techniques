import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
input_data = torch.from_numpy(input_data)
output = torch.acos(input_data)