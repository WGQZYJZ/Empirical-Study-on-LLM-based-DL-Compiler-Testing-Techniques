'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.Tensor.mv\ntorch.Tensor.mv(_input_tensor, vec)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
_input_tensor = torch.randn(2, 3)
vec = torch.randn(3)
torch.Tensor.mv(_input_tensor, vec)