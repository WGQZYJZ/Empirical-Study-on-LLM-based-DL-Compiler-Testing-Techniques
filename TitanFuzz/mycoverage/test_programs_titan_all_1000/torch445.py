import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float)
tensor2 = torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.double)
torch.result_type(tensor1, tensor2)