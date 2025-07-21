'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_unpool1d\ntorch.nn.functional.max_unpool1d(input, indices, kernel_size, stride=None, padding=0, output_size=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 4, 4))
indices = Variable(torch.LongTensor([[[1, 2, 1, 2], [2, 1, 2, 1], [1, 2, 1, 2], [2, 1, 2, 1]]]))
kernel_size = 2
output = torch.nn.functional.max_unpool1d(input, indices, kernel_size)
print('output = ', output)