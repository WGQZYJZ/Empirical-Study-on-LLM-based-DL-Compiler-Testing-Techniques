import torch
from torch import nn
from torch.autograd import Variable
input_data = np.array([(- 1), 2, 3, 5])
input_data = torch.tensor(input_data, dtype=torch.float32)
output = torch.nn.functional.leaky_relu_(input_data, negative_slope=0.01)