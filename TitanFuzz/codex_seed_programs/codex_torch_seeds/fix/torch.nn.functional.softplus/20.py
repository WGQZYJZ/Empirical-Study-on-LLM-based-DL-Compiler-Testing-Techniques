'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softplus\ntorch.nn.functional.softplus(input, beta=1, threshold=20)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.randn(5, 5))
print(x)
print(torch.nn.functional.softplus(x))