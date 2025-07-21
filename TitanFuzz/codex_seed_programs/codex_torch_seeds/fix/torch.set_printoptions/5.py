'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.set_printoptions\ntorch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)\n'
import torch
from torch.autograd import Variable
x_data = Variable(torch.Tensor([[1.0, 1.0], [2.0, 2.0], [3.0, 3.0]]))
y_data = Variable(torch.Tensor([[2.0, 2.0], [4.0, 4.0], [6.0, 6.0]]))
torch.set_printoptions(precision=None, threshold=None, edgeitems=None, linewidth=None, profile=None, sci_mode=None)