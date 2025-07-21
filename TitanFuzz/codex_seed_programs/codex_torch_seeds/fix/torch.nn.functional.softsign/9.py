'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softsign\ntorch.nn.functional.softsign(input)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(5, 5))
output = torch.nn.functional.softsign(input_data)
print(output)
'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.softshrink\ntorch.nn.functional.softshrink(input, lambd=0.5)\n'
import torch
from torch.autograd import Variable
import torch
input_data = Variable(torch.randn(5, 5))
output = torch.nn.functional.softshrink(input_data)
print(output)