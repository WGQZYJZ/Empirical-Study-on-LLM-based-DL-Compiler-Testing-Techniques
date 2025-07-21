'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.FractionalMaxPool3d\ntorch.nn.FractionalMaxPool3d(kernel_size, output_size=None, output_ratio=None, return_indices=False, _random_samples=None)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(20, 16, 50, 32, 32))
pool = torch.nn.FractionalMaxPool3d(kernel_size=(2, 3, 3), output_size=(10, 16, 16))
output = pool(input)
print(output.shape)