'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
from torch.nn import functional as F
input = Variable(torch.randn(1, 1, 3, 3))
output = F.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)
print(output)