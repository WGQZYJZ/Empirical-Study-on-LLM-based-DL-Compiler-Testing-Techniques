import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
identity_layer = torch.nn.Identity()
output = identity_layer(input_data)