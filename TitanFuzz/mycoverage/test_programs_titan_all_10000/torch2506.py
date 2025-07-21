import torch
from torch import nn
from torch.autograd import Variable
input_data = np.random.randn(5, 3)
input_data = torch.tensor(input_data, dtype=torch.float)
torch.nn.init.kaiming_normal_(input_data, a=0, mode='fan_in', nonlinearity='leaky_relu')