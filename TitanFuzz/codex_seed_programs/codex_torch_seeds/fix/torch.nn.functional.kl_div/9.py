"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.kl_div\ntorch.nn.functional.kl_div(input, target, size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.randn(2, 3))
target = Variable(torch.randn(2, 3))
torch.nn.functional.kl_div(input, target)
print(torch.nn.functional.kl_div(input, target))
print(torch.nn.functional.kl_div(input, target).size())