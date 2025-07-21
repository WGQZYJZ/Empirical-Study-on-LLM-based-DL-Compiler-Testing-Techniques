'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.selu\ntorch.nn.functional.selu(input, inplace=False)\n'
import torch
from torch.autograd import Variable
import numpy as np
import torch.nn.functional as F
input = Variable(torch.FloatTensor(np.random.rand(2, 3)))
output = F.selu(input)
print(output)