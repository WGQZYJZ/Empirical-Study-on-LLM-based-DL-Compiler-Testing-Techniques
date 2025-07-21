import torch
from torch import nn
from torch.autograd import Variable
np.random.seed(0)
input_data = np.random.randn(5)
input_tensor = torch.tensor(input_data)
softplus = torch.nn.Softplus()
output = softplus(input_tensor)