'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mvlgamma_\ntorch.Tensor.mvlgamma_(_input_tensor, p)\n'
import torch
from torch.autograd import Variable
_input_tensor = Variable(torch.randn(4, 4))
p = 3
torch.Tensor.mvlgamma_(_input_tensor, p)