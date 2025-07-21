'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.Bilinear\ntorch.nn.Bilinear(in1_features, in2_features, out_features, bias=True, device=None, dtype=None)\n'
import torch
from torch.autograd import Variable
input1 = Variable(torch.randn(2, 3))
input2 = Variable(torch.randn(2, 3))
bilinear = torch.nn.Bilinear(3, 3, 1)
output = bilinear(input1, input2)
print(output)