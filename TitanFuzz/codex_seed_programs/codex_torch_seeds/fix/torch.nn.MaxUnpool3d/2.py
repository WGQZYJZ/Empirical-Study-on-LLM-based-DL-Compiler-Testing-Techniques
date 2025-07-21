'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.MaxUnpool3d\ntorch.nn.MaxUnpool3d(kernel_size, stride=None, padding=0)\n'
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor([[[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]]]))
indices = Variable(torch.LongTensor([[[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]]))
output = torch.nn.MaxUnpool3d(kernel_size=2)(input, indices)
print(output)
'\noutput:\nVariable containing:\n(0 ,0 ,.,.) =\n   1   2   3   4\n   5   6   7   8\n   9  10  11  12\n  13  14  15  16\n[torch.FloatTensor of size 1x1x4x4]\n'