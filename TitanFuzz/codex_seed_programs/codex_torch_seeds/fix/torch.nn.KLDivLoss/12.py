"\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.KLDivLoss\ntorch.nn.KLDivLoss(size_average=None, reduce=None, reduction='mean', log_target=False)\n"
import torch
from torch.autograd import Variable
import numpy as np
import torch
from torch.autograd import Variable
import numpy as np
input = Variable(torch.randn(3, 5), requires_grad=True)
target = Variable(torch.randn(3, 5))
loss = torch.nn.KLDivLoss()
output = loss(input, target)
print(output)