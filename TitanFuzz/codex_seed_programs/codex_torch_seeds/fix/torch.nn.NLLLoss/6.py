"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.NLLLoss\ntorch.nn.NLLLoss(weight=None, size_average=None, ignore_index=-100, reduce=None, reduction='mean')\n"
import torch
import torch.nn as nn
import numpy as np
input = torch.autograd.Variable(torch.randn(3, 5), requires_grad=True)
target = torch.autograd.Variable(torch.LongTensor(3).random_(5))
output = nn.NLLLoss()(input, target)
output.backward()
print(input.grad)
'\nTask 5: print the loss\nTask 6: print the gradients d(output)/dx\n'
import torch
import torch.nn as nn
import numpy as np