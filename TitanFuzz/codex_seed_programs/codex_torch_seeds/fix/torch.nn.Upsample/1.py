"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Upsample\ntorch.nn.Upsample(size=None, scale_factor=None, mode='nearest', align_corners=None)\n"
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.Tensor(1, 1, 3, 3))
input[0, 0, :, :] = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
upsample = torch.nn.Upsample(scale_factor=2, mode='nearest')
output = upsample(input)
print('input: ', input)
print('output: ', output)