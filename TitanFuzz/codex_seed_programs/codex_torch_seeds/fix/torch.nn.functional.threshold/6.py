'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.threshold\ntorch.nn.functional.threshold(input, threshold, value, inplace=False)\n'
import torch
from torch.autograd import Variable
import torch
x = Variable(torch.Tensor([[1, 2, 3, 4], [5, 6, 7, 8]]))
y = torch.nn.functional.threshold(x, threshold=3, value=0)
print(y)
print(y)