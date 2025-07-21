import torch
from torch import nn
from torch.autograd import Variable
input_data = [1, 2, 3, 4, 5]
input_tensor = torch.tensor(input_data)
input_storage = torch.QUInt8Storage(input_data)