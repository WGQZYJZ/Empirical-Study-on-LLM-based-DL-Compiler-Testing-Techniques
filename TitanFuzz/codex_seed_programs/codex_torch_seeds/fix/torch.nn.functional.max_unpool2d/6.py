'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.max_unpool2d\ntorch.nn.functional.max_unpool2d(input, indices, kernel_size, stride=None, padding=0, output_size=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(1, 1, 2, 2))
indices = Variable(torch.LongTensor([[[[0, 1], [1, 0]]]]))
output = torch.nn.functional.max_unpool2d(input, indices, kernel_size=2, stride=1, padding=0)
print(output)