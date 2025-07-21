'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool1d\ntorch.nn.MaxUnpool1d(kernel_size, stride=None, padding=0)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input = Variable(torch.Tensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
indices = Variable(torch.LongTensor([[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]]))
max_unpool = torch.nn.MaxUnpool1d(kernel_size=2, stride=2, padding=0)
output = max_unpool(input, indices)
print(output)