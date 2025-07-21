"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.pad\ntorch.nn.functional.pad(input, pad, mode='constant', value=0)\n"
import torch
from torch.autograd import Variable
import torch
input = Variable(torch.FloatTensor([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]]))
padding = (0, 2, 1, 0)
print(torch.nn.functional.pad(input, padding, mode='constant', value=0))