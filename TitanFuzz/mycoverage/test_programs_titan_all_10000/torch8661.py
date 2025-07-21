import torch
from torch import nn
from torch.autograd import Variable
input_data = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32)
output_data = torch.nn.functional.log_softmax(input_data, dim=1)