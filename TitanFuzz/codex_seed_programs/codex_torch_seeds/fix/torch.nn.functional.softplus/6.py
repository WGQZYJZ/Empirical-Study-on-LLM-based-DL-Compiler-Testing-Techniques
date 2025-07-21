'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input = Variable(torch.randn(3))
output = torch.nn.functional.softplus(input)
print(output)
output = torch.nn.functional.softplus(input, beta=1, threshold=20)
print(output)