import torch
from torch import nn
from torch.autograd import Variable
tensor1 = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
tensor2 = torch.tensor([[5, 6], [7, 8]], dtype=torch.int64)
torch.result_type(tensor1, tensor2)