import torch
from torch import nn
from torch.autograd import Variable
input_tensor = torch.tensor([[True, False, True], [False, True, False]], dtype=torch.bool)
other_tensor = torch.tensor([[True, True, False], [False, False, True]], dtype=torch.bool)
torch.Tensor.bitwise_xor_(input_tensor, other_tensor)