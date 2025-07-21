'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_unpool2d\ntorch.nn.functional.max_unpool2d(input, indices, kernel_size, stride=None, padding=0, output_size=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import numpy as np
import torch
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
indices = Variable(torch.LongTensor([[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]]))
output = F.max_unpool2d(input, indices, 2, stride=2, padding=0)
print(output)