'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.log_softmax\ntorch.nn.functional.log_softmax(input, dim=None, _stacklevel=3, dtype=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
x = Variable(torch.randn(1, 5))
print(x)
torch.nn.functional.log_softmax(x)