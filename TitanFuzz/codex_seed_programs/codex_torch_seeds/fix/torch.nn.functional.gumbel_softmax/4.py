'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.gumbel_softmax\ntorch.nn.functional.gumbel_softmax(logits, tau=1, hard=False, eps=1e-10, dim=-1)\n'
import torch
from torch.autograd import Variable
import torch
from torch.autograd import Variable
input_data = Variable(torch.randn(2, 3))
print(torch.nn.functional.gumbel_softmax(input_data, tau=0.1, hard=False))
print(torch.nn.functional.gumbel_softmax(input_data, tau=0.1, hard=True))
print(torch.nn.functional.gumbel_softmax(input_data, tau=1, hard=False))
print(torch.nn.functional.gumbel_softmax(input_data, tau=1, hard=True))
print(torch.nn.functional.gumbel_softmax(input_data, tau=10, hard=False))
print(torch.nn.functional.gumbel_softmax(input_data, tau=10, hard=True))