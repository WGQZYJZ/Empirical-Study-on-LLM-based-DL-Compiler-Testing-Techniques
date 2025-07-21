'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.elu\ntorch.nn.functional.elu(input, alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
data = Variable(torch.Tensor([(- 1), (- 0.5), 0, 1, 2]))
print(torch.nn.functional.elu(data))