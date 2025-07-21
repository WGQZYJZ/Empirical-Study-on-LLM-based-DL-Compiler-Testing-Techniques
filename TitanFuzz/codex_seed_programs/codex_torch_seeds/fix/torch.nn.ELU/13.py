'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.ELU\ntorch.nn.ELU(alpha=1.0, inplace=False)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.Tensor([(- 1), 0, 1]))
y = torch.nn.ELU()(x)
print(y)