'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.upsample_nearest\ntorch.nn.functional.upsample_nearest(input, size=None, scale_factor=None)\n'
import torch
from torch.autograd import Variable
import torch.nn.functional as F
import torch
input = Variable(torch.Tensor(1, 1, 3, 3))
input[0, 0, :, :] = torch.Tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
output = F.upsample_nearest(input, size=None, scale_factor=2)
print(output)