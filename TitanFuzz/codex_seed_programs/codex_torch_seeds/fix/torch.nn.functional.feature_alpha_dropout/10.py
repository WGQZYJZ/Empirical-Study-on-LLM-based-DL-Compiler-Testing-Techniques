'\nTask 1: import PyTorch\nTask 2: Generate input data\nTask 3: Call the API torch.nn.functional.feature_alpha_dropout\ntorch.nn.functional.feature_alpha_dropout(input, p=0.5, training=False, inplace=False)\n'
import torch
from torch.autograd import Variable
x = Variable(torch.ones(1, 1, 1, 1))
print(x)
y = torch.nn.functional.feature_alpha_dropout(x, p=0.5)
print(y)
y = torch.nn.functional.feature_alpha_dropout(x, p=0.5, training=True)
print(y)